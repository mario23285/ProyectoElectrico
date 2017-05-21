HIERARCHY
ROOT Hips
{
	OFFSET 0.00 0.00 0.00
	CHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation
	JOINT Chest
	{
		OFFSET 5.00 0.00 0.00
		CHANNELS 3 Zrotation Xrotation Yrotation
		End Site
		{
			OFFSET 0.00 5.00 0.00
		}
	}
	JOINT Leg
	{
		OFFSET -5.0 0.0 0.0
		CHANNELS 3 Zrotation Xrotation Yrotation
		End Site
		{
			OFFSET 0.0 5.0 0.0
		}
	}
}
MOTION
Frames:		2
Frame Time: 0.033333
 0.00 0.00 0.00 0.00 0.00 0.00  0.00 0.00 0.00  0.00 0.00 0.00
 0.00 0.00 0.00 0.00 0.00 0.00  0.00 45.00 0.00  0.00 0.00 0.00

 /*--------------------------------------------------------------------------*/

#define Xposition 0x01
#define Yposition 0x02
#define Zposition 0x04
#define Zrotation 0x10
#define Xrotation 0x20
#define Yrotation 0x40

typedef struct
{
    float x, y, z;
} OFFSET;

typedef struct JOINT JOINT;

struct JOINT
{
    const char* name = NULL;        // joint name
    JOINT* parent = NULL;           // joint parent
    OFFSET offset;                  // offset data
    unsigned int num_channels = 0;  // num of channels joint has
    short* channels_order = NULL;   // ordered list of channels
    std::vector<JOINT*> children;   // joint's children
    glm::mat4 matrix;               // local transofrmation matrix (premultiplied with parents'
    unsigned int channel_start = 0; // index of joint's channel data in motion array
};

typedef struct
{
    JOINT* rootJoint;
    int num_channels;
} HIERARCHY;

typedef struct
{
    unsigned int num_frames;              // number of frames
    unsigned int num_motion_channels = 0; // number of motion channels
    float* data = NULL;                   // motion float data array
    unsigned* joint_channel_offsets;      // number of channels from beggining of hierarchy for i-th joint
} MOTION;
