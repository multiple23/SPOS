#include <jni.h>
#ifndef _Included_SampleDLL
#define _Included_SampleDLL
#ifdef __cplusplus

extern "C"{
#endif
JNIEXPORT jint JNICALL Java_SampleDLL_add
  (JNIEnv *, jObject, jint, jint);

#ifdef __cplusplus
}
#endif
#endif