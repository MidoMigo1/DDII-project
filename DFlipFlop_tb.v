`timescale 1ns/1ps

 module DFlipFlop _tb;

//inputs 
 reg clk ;  
 reg rst ;  
 reg D ;  
 
 //outputs 
 wire Q ; 

 // Instantiation of Unit Under Test 
DFlipFlop uut (
   .clk(clk), 
   .rst(rst), 
   .D(D), 
   .Q(Q), 
);
 
initial begin 
   forever begin
   clk=0; 
   #10  clk= ~clk;
   end 
 end

initial begin 
$monitor("clk%d rst%d D%d Q%d \linitial begin 
 //Inputs initialization 
   clk = 0;
   rst = 0;
   D = 0;

 
 initial begin 
     $dumpfile(DFlipFlop.vcd); 
     s$dumpvars; 
end
Wait for the reset 
  #100, 

  end 

 endmodule 
