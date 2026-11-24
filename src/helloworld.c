#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "platform.h"
#include "xil_printf.h"
#include "xparameters.h"
#include "xtmrctr.h"
#include "image_data.h"

/* Define image dimensions: WIDTH (160), HEIGHT (120), and TOTAL_PIXELS. */
/* Declare a zero-initialized global output buffer to hold the resulting image pixels (Sobel outputs). */

#define TIMER_DEV_ID XPAR_TMRCTR_0_DEVICE_ID
XTmrCtr TimerInstance;

void sw_sobel() {
    
    /* Apply 3x3 Sobel on image_data.h data (x:WIDTH, y:HEIGHT)
     * Compute magnitude as (abs(gx) + abs(gy)) / 4 and clamp to 255. */

}

void send_image_over_uart() {
    /* Send Sobel data over UART using `xil_printf`:
     * Print "START_IMAGE\r\n", then each pixel ("%d\r\n") for TOTAL_PIXELS,
     * and finish with "END_IMAGE\r\n". */

}

int main() {
    
    u32 t_start, t_end, sw_cycles;

    init_platform();

    if (XTmrCtr_Initialize(&TimerInstance, TIMER_DEV_ID) != XST_SUCCESS) {
        xil_printf("Timer Initialization Failed!\r\n");
        cleanup_platform();
        return -1;
    }

    /* You can measure `sw_sobel()` clock cycles using AXI Timer functions:
     * `XTmrCtr_Start`, `XTmrCtr_GetValue`, and `XTmrCtr_Stop`
     * (inputs: `&TimerInstance` as instance pointer, `0` as timer number).
     * You can print total cycles with `xil_printf` and call `send_image_over_uart(). */

    cleanup_platform();
    return 0;
}