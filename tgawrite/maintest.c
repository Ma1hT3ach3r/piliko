// test of tgawrite.h
// see license.txt for license

#include "tgawrite.h"

int main() {
	uint16_t w = 256;
	uint16_t h = 256;
	uint32_t pixels[w*h];
	for (int i=0;i<w;i++) {
		for (int j=0;j<h;j++) {
			pixels[w*j+i] = i*i+j*j;
		}
	}
	tgawrite("test.tga",pixels,w,h);
}