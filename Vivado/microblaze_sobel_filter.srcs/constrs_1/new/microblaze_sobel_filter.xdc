set_property PACKAGE_PIN U18 [get_ports clk_in1_0]
set_property IOSTANDARD LVCMOS33 [get_ports clk_in1_0]
create_clock -period 20.000 -name clk_in1_0 -waveform {0.000 10.000} [get_ports clk_in1_0]

set_property PACKAGE_PIN R14 [get_ports reset_rtl_0]
set_property IOSTANDARD LVCMOS33 [get_ports reset_rtl_0]

## -----------------------------------------------------------------------------
## 3. UART Interface (AXI UARTLite @ 115200 bps)
##    Connected to external USB-UART module via 40-pin header:
##    - uart_rtl_0_rxd (FPGA RX <- USB-UART Module TX): Pin P14
##    - uart_rtl_0_txd (FPGA TX -> USB-UART Module RX): Pin P15
## -----------------------------------------------------------------------------

set_property PACKAGE_PIN P14 [get_ports uart_rtl_0_rxd]
set_property IOSTANDARD LVCMOS33 [get_ports uart_rtl_0_rxd]

set_property PACKAGE_PIN P15 [get_ports uart_rtl_0_txd]
set_property IOSTANDARD LVCMOS33 [get_ports uart_rtl_0_txd]
