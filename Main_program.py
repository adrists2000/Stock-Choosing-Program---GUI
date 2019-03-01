import Gui
import Scrap_eps
import Scrap_eps2
import Scrap_price
import Scrap_roe
import Scrap_cashflow

EXE=1
while EXE==1:
    LIST_INPUT,COND,PRIORITY,EXE,GPRINT = Gui.Main_gui() 
    if EXE==1:
        for I in PRIORITY:
            if   I==("a"):
                LIST_OUTPUT=Scrap_eps.Main_eps(LIST_INPUT,COND[1],GPRINT)
            elif I==("b"):
                LIST_OUTPUT=Scrap_eps2.Main_eps2(LIST_INPUT,COND[2],GPRINT) 
            elif I=="c" or I=="d":
                LIST_OUTPUT=Scrap_price.Main_price(LIST_INPUT,COND[3],COND[4],I,GPRINT) 
            elif I=="e":        
                LIST_OUTPUT=Scrap_roe.Main_roe(LIST_INPUT,COND[5],GPRINT)
            elif I=="f":
                LIST_OUTPUT=Scrap_cashflow.Main_cashflow(LIST_INPUT,COND[6],GPRINT)
            if COND[0]:    
                LIST_INPUT=LIST_OUTPUT  
        EXE=Gui.End_gui(COND[0],LIST_OUTPUT)
        
 
        








