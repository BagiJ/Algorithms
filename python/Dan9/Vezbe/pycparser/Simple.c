#include <stdint.h>
#include <stdbool.h>

#define MACRO 100
#define macro_test {TRUE, FALSE}
#define D1 5
#define D2 10

typedef enum
{
	elem1,
	elem2 = 0,
	elem3
}
tEnumTest;

typedef enum EnumTest2
{
	elem11,
	elem21,
	elem31
}tEnumTest2;

typedef enum EnumTest3
{
	first,
	second,
	third = 5
}tEnumTest3;

typedef int32_t Dt_ARRAY12_UINT32_1_0[12];

typedef struct
{
	int8_t 		ddarrayStruct1 [D1][D2];
	int8_t		var1;
	int16_t		var2;
    int32_t  	var3;
	uint8_t		array1[5];
	uint16_t	var5;
    uint32_t  	var6;
    float    	var7;
    bool        var8;
    tEnumTest 	var9;
}tStructure1;

typedef struct
{
    int16_t		var1;
    int16_t		var2;
    int32_t  	array4[10];
    uint32_t  	array5[2];
    float    	var7;
    tStructure1 *vpStructure1_5;
    tStructure1  vStructure1_1[1];
    union Data
    {
       int i;
       float f;
       int8_t  str[20];
       tStructure1 vStructure1;
    } tData;
}tStructure2;

struct Structure3
{
	int8_t x;
	int8_t y;
};

typedef struct
{
	tStructure2 Data;
}tStructure4;

typedef uint8_t check_shm_size[sizeof (tStructure1) > 369848 ? 1 : 1];

/***************************************************************************************/

union Data2
{
   int i;
   float f;
   int8_t  str[20];
} tData2;

static int8_t ddarray [8][18];
static int32_t testVal;	
static float n;
static int8_t array[] = {3, 4, 3, 2};
static int8_t array2[100];
static float array3[] = {1, 4, 7, 2, 8, 0};
static int8_t txt = 'c';
static bool boolean_var;
static int m = MACRO;

static int function4();

int16_t val = elem2;
int16_t val2 = elem21;

static int8_t vArray[second];

static struct Structure3 tStructure3;

static tStructure1  vStructure1_2[3];
static tStructure2  vStructure2_1[1];
static tStructure1  vStructure1_3[1];
static tStructure2  vStructure2_2;

tStructure1 *vpStructure1_1 = &vStructure1_3[0];
tStructure1 *vpStructure1_7 = &vStructure1_3[0];

static tStructure2 vStruct;
static int bak[sizeof(tStructure2)];

/***************************************************************************************/
void function1 ()
{
	typedef struct
	{
		int16_t                  Position;
		int16_t                  Length;
	}
	tBufSpec;
	const tBufSpec          vTestSpec[] =
			{ {   0,   5 }, {   3,   5 }, {   4,   5 }
			, {   0, 176 }, { 103, 176 }, { 104, 176 }
			, {   0, 262 }, { 203, 262 }, { 204, 262 }
			};
	if (d);
	if (c)
	{
		int x = 9;
	}
	else;

	for (i = 0; i < 3; i++)
		i += 1;

	tStructure4 vStructure4;
	tStructure2 * vpStructure2_3 = &vStructure4.Data;

	vpStructure2_3 -> tData.i = 5;
}

int function2(int m, tStructure1 *vpStructure1_3){

	vpStructure1_3 -> var3 = 4;
	int s;
	int h;

	switch(n)
	{
		case 1 :
		{
			int32_t x = 1;
			int32_t x_1 = 1;
			uint8_t x_2 = 4;

			if (x == 1)
			{
				(&vStructure2_2) -> array5 [0] = 2;
				return 0;
			}

			break;
		}

		case 2:
		{
			break;
		}

		case 3:
		{
			int16_t y = 2;
			float c;
			break;
		}
		default:
		{
			int z = 4;
			break;
		}
	}

	memset(&bak[0], 0x00, sizeof(tStructure2));
	tStructure1 vStructure1;
	tStructure1 * vpStructure1_2 = &vStructure1[0];
	vpStructure1_2 -> array1[3]++;
	int i = 5;
	return z;
}


void function3()
{
	int n = 3;
	int c = 3;
	if (c == 4)
	{
		if (n == 3)
		{
			int32_t x = 5;
			int32_t y = 5;
			if (m = 2)
			{
				int32_t t = 2;
				int32_t h = 5;
			}
			else
			{
				int32_t h = 5;
			}
		}
	}
	else if (c == 2)
	{
		int8_t y = 1;
		int8_t x = 1;
	}
	else if (c == 7)
	{
		int8_t x = 2;
	}
	else
	{
		int8_t x = 6;
		int w = 54;
	}

	switch(n)
	{
		case 1 :
			if (x == 1)
			{
				{
					(&vStructure2_2) -> array5 [0] = 2;
					(&vStructure2_2) -> var1 = 2;
				}
				if (m = 2)
				{
					int32_t t = 2;
					int32_t h = 5;
				}
				else
				{
					int32_t h = 5;
					long h = 3;
				}
			}
			else
			{
				int i;
			}
			break;

		case 2:

			break;

		default:
			break;
	}
}

int function4()
{
	tEnumTest vEnumTest;

	vEnumTest.elem1 = 3;

	int16_t	*vpStructure2;
	tStructure2  vStructure2;

	*vpStructure2 = vStructure2.var1;

	int i;
	int retVar;
	int y;
	n = 3;
	;
	while (y < 5)
	{
		y += 1;
	}
	tStructure2 * vpStructure2_1 = &vStructure2_1[0];
	{
		int vTest;
		i = 4;
		if (n = 5)
		{
			function1();
			i++;
			testVal = 10;
			vpStructure2_1->vStructure1_1.var2 = 5;
			vpStructure2_1->vStructure1_1.var1++;
			retVar = function2();
		}
		int m = 10;
		float x = 1.2;
	}
	int s;
	int h;
	if (y)
	{
		int vTest;
		y = 3;
		for (int g = 0; g < 5 ; g++ )
		{
			h = s + 20;
		}
	}

	static struct Structure3 tStructure3;
	static tStructure1 vStructure1_4;
	function3();
	return i;
}

void main()
{
	function2();

	function3();

	function4();
}
