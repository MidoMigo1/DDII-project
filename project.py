import hdlparse.verilog_parser as vlog



vlog_ex = vlog.VerilogExtractor()
with open("test.v", 'rt') as fh:
  code = fh.read()
vlog_mods = vlog_ex.extract_objects_from_source(code)
vlog_mods = vlog_ex.extract_objects("test.v")

for m in vlog_mods: 
    x = (m.name)
    x= x + '_tb.v'
    f = open(x,"w")
    f.write("`timescale 1ns/1ps")
    f.write("\n\n module " + m.name +" _tb;\n")
    f.write('\n')
    f.write('//inputs \n')
    for p in m.ports :
        if p.mode == "input":
            f.write(" reg " + p.name +" ;  \n")
    f.write(' \n ')
    f.write('//outputs \n')
    for p in m.ports :        
        if p.mode == "output":
           f.write(" wire " + p.name + " ; \n")
    f.write('\n ')
    f.write('// Instantiation of Unit Under Test \n')
    f.write(m.name +' uut (\n')
    for p in m.ports:
        f.write("   ." + p.name + "(" + p.name +"), \n")
    f.write(');')
    f.write('\n \n')
    for p in m.ports:
        if p.name == "clk":
            z = True 
            if (z):
                f.write("initial begin \n   forever begin\n   clk=0; \n   #10  clk= ~clk;\n   end \n end\n\n")
        if p.name == "CLK":
            z = True 
            if (z):
                f.write("initial begin \n   forever begin\n   CLK=0; \n   #10  CLK= ~CLK;\n   end \n end\n\n")
        if p.name == "clock":
            z = True 
            if (z):
                f.write("initial begin \n   forever begin\n   clock=0; \n   #10  clock= ~clock;\n   end \n end\n\n")
        if p.name == "CLOCK":
            z = True 
            if (z):
                f.write("initial begin \n   forever begin\n   CLOCK=0; \n   #10  CLOCK= ~CLOCK;\n   end \n end\n\n")       
    f.write( 'initial begin \n')
    x ='$monitor("'
    for p in m.ports:
        y=(p.name)
        x= x + y +"%d "
    f.write(x)
    f.write('\l')
    f.write('initial begin \n //Inputs initialization \n')
    for p in m.ports:
        if p.mode == "input":
            f.write("   " + p.name + " = 0;\n") 
    f.write('\n \n') 
    f.write(" initial begin \n     $dumpfile("+ m.name +".vcd); \n     $dumpvars; \n end\n")
    f.write('Wait for the reset \n  #100, \n\n  end \n\n endmodule \n')
   
    
    
        