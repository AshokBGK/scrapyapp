# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()

from bs4 import BeautifulSoup
html = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
<HEAD>
<TITLE>Page 1</TITLE>

<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<DIV style="position:relative;width:918;height:1188;">
<STYLE type="text/css">
<!--
	.ft0{virtical-align:top;font-size:22px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:0.00000px;}
	.ft1{virtical-align:top;font-size:22px;font-family:Times;color:#000000;letter-spacing:0.00000px;}
	.ft2{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:0.00000px;}
	.ft3{virtical-align:top;font-size:4px;font-family:Times;color:#000000;letter-spacing:0.00000px;}
	.ft4{virtical-align:top;font-size:7px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:0.00000px;}
	.ft5{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:0.00000px;}
	.ft6{virtical-align:top;font-size:16px;font-family:Times;color:#000000;letter-spacing:0.00000px;}
	.ft7{virtical-align:top;font-size:13px;font-family:Times;color:#cc6420;letter-spacing:0.00000px;}
	.ft8{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:0.00000px;}
	.ft9{virtical-align:top;font-size:7px;font-family:Times;color:#ffffff;letter-spacing:0.00000px;}
	.ft10{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.00000px;}
	.ft11{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.00000px;}
	.ft12{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.00000px;}
	.ft13{virtical-align:top;font-size:6px;font-family:Times;color:#e4801b;letter-spacing:0.00000px;}
	.ft14{virtical-align:top;font-size:4px;font-family:Times;color:#ffffff;letter-spacing:0.00000px;}
	.ft15{virtical-align:top;font-size:2px;font-family:Times;color:#000000;letter-spacing:0.00000px;}
	.ft16{virtical-align:top;font-size:19px;font-family:Times;color:#ff0000;letter-spacing:0.00000px;}
	.ft17{virtical-align:top;font-size:1px;font-family:Times;color:#ff0000;letter-spacing:0.00000px;}
	.ft18{virtical-align:top;font-size:22px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:0.78086px;}
	.ft19{virtical-align:top;font-size:22px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:0.76188px;}
	.ft20{virtical-align:top;font-size:22px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:0.74109px;}
	.ft21{virtical-align:top;font-size:22px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:0.74274px;}
	.ft22{virtical-align:top;font-size:22px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:0.75338px;}
	.ft23{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.36697px;}
	.ft24{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.34892px;}
	.ft25{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.33502px;}
	.ft26{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.54941px;}
	.ft27{virtical-align:top;font-size:7px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.25257px;}
	.ft28{virtical-align:top;font-size:7px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.14706px;}
	.ft29{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:1.55634px;}
	.ft30{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:1.23283px;}
	.ft31{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:1.52222px;}
	.ft32{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:1.21767px;}
	.ft33{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:1.09135px;}
	.ft34{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:1.08251px;}
	.ft35{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:1.55634px;}
	.ft36{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:1.23283px;}
	.ft37{virtical-align:top;font-size:16px;font-family:Times;color:#000000;letter-spacing:0.82160px;}
	.ft38{virtical-align:top;font-size:13px;font-family:Times;color:#cc6420;letter-spacing:0.86191px;}
	.ft39{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:1.24122px;}
	.ft40{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:1.12160px;}
	.ft41{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:0.88664px;}
	.ft42{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:0.86825px;}
	.ft43{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:0.91468px;}
	.ft44{virtical-align:top;font-size:7px;font-family:Times;color:#ffffff;letter-spacing:0.96021px;}
	.ft45{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.32321px;}
	.ft46{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.22131px;}
	.ft47{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.17425px;}
	.ft48{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09777px;}
	.ft49{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06230px;}
	.ft50{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06874px;}
	.ft51{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05918px;}
	.ft52{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03828px;}
	.ft53{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01998px;}
	.ft54{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02246px;}
	.ft55{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02423px;}
	.ft56{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02679px;}
	.ft57{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02045px;}
	.ft58{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.23872px;}
	.ft59{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.15119px;}
	.ft60{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05623px;}
	.ft61{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01986px;}
	.ft62{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03593px;}
	.ft63{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03548px;}
	.ft64{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03504px;}
	.ft65{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03565px;}
	.ft66{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04605px;}
	.ft67{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03745px;}
	.ft68{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02879px;}
	.ft69{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.25235px;}
	.ft70{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.12882px;}
	.ft71{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05847px;}
	.ft72{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03082px;}
	.ft73{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02381px;}
	.ft74{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.00851px;}
	.ft75{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01456px;}
	.ft76{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01073px;}
	.ft77{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02817px;}
	.ft78{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02118px;}
	.ft79{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.23695px;}
	.ft80{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.08218px;}
	.ft81{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03076px;}
	.ft82{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01216px;}
	.ft83{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01670px;}
	.ft84{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01676px;}
	.ft85{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03835px;}
	.ft86{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02855px;}
	.ft87{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02958px;}
	.ft88{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.00952px;}
	.ft89{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01066px;}
	.ft90{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.27264px;}
	.ft91{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.17373px;}
	.ft92{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.14111px;}
	.ft93{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09751px;}
	.ft94{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04930px;}
	.ft95{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05844px;}
	.ft96{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04611px;}
	.ft97{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03212px;}
	.ft98{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03462px;}
	.ft99{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03236px;}
	.ft100{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02187px;}
	.ft101{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.15775px;}
	.ft102{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.08900px;}
	.ft103{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03698px;}
	.ft104{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02516px;}
	.ft105{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.00676px;}
	.ft106{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.97108px;}
	.ft107{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.96703px;}
	.ft108{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.97400px;}
	.ft109{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.97842px;}
	.ft110{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.97299px;}
	.ft111{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.08300px;}
	.ft112{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.97932px;}
	.ft113{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.00320px;}
	.ft114{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.34622px;}
	.ft115{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:1.32107px;}
	.ft116{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:1.17020px;}
	.ft117{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:1.02056px;}
	.ft118{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.99964px;}
	.ft119{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.95230px;}
	.ft120{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.92460px;}
	.ft121{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.92048px;}
	.ft122{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.90591px;}
	.ft123{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.86220px;}
	.ft124{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.87885px;}
	.ft125{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.87829px;}
	.ft126{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.86866px;}
	.ft127{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.85515px;}
	.ft128{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.87228px;}
	.ft129{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.87241px;}
	.ft130{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:1.05300px;}
	.ft131{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.93690px;}
	.ft132{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.87852px;}
	.ft133{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.84954px;}
	.ft134{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.84615px;}
	.ft135{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.83847px;}
	.ft136{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.93713px;}
	.ft137{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.86428px;}
	.ft138{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.84548px;}
	.ft139{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.82950px;}
	.ft140{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.82735px;}
	.ft141{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.83117px;}
	.ft142{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.82681px;}
	.ft143{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.89394px;}
	.ft144{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.84352px;}
	.ft145{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.80709px;}
	.ft146{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.81416px;}
	.ft147{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.82021px;}
	.ft148{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.81654px;}
	.ft149{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.82873px;}
	.ft150{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.83227px;}
	.ft151{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.97875px;}
	.ft152{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.88542px;}
	.ft153{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.88375px;}
	.ft154{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.86381px;}
	.ft155{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.85416px;}
	.ft156{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.85586px;}
	.ft157{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.87222px;}
	.ft158{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.95259px;}
	.ft159{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.85894px;}
	.ft160{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.82902px;}
	.ft161{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.83018px;}
	.ft162{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.83285px;}
	.ft163{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.82138px;}
	.ft164{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.82501px;}
	.ft165{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.90795px;}
	.ft166{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.86901px;}
	.ft167{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.84465px;}
	.ft168{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.87470px;}
	.ft169{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.87464px;}
	.ft170{virtical-align:top;font-size:9px;font-family:Times;color:#000000;letter-spacing:0.88300px;}
	.ft171{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.23529px;}
	.ft172{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:1.30192px;}
	.ft173{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:1.06145px;}
	.ft174{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:1.07224px;}
	.ft175{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:1.01941px;}
	.ft176{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.15658px;}
	.ft177{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.05370px;}
	.ft178{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.04392px;}
	.ft179{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.09313px;}
	.ft180{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:1.05902px;}
	.ft181{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:0.99826px;}
	.ft182{virtical-align:top;font-size:7px;font-family:Times;color:#6e6e70;letter-spacing:0.98852px;}
	.ft183{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:0.95400px;}
	.ft184{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:1.20412px;}
	.ft185{virtical-align:top;font-size:7px;font-family:Times;color:#000000;letter-spacing:1.14058px;}
	.ft186{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.09331px;}
	.ft187{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.06404px;}
	.ft188{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.27954px;}
	.ft189{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.17741px;}
	.ft190{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.14369px;}
	.ft191{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.10950px;}
	.ft192{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.06873px;}
	.ft193{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.02013px;}
	.ft194{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.04555px;}
	.ft195{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.31175px;}
	.ft196{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.11394px;}
	.ft197{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.13876px;}
	.ft198{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.15594px;}
	.ft199{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.17551px;}
	.ft200{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.15868px;}
	.ft201{virtical-align:top;font-size:7px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.16077px;}
	.ft202{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.19875px;}
	.ft203{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.08057px;}
	.ft204{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.20269px;}
	.ft205{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.15086px;}
	.ft206{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.31213px;}
	.ft207{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.13741px;}
	.ft208{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.09652px;}
	.ft209{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.10072px;}
	.ft210{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.04965px;}
	.ft211{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.03425px;}
	.ft212{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.02042px;}
	.ft213{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.16603px;}
	.ft214{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.21472px;}
	.ft215{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.11017px;}
	.ft216{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.10605px;}
	.ft217{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.19044px;}
	.ft218{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.19044px;}
	.ft219{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.34859px;}
	.ft220{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.12462px;}
	.ft221{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.11222px;}
	.ft222{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.06872px;}
	.ft223{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.02012px;}
	.ft224{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.04555px;}
	.ft225{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.18706px;}
	.ft226{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.10053px;}
	.ft227{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.11980px;}
	.ft228{virtical-align:top;font-size:7px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.19331px;}
	.ft229{virtical-align:top;font-size:7px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.17882px;}
	.ft230{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.10266px;}
	.ft231{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.07612px;}
	.ft232{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.03873px;}
	.ft233{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.01510px;}
	.ft234{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.62750px;}
	.ft235{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.19737px;}
	.ft236{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.36664px;}
	.ft237{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.21472px;}
	.ft238{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.15762px;}
	.ft239{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.15537px;}
	.ft240{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.33275px;}
	.ft241{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.20269px;}
	.ft242{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.57448px;}
	.ft243{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.15806px;}
	.ft244{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.21800px;}
	.ft245{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.16616px;}
	.ft246{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.08596px;}
	.ft247{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.31175px;}
	.ft248{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.11394px;}
	.ft249{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.13876px;}
	.ft250{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.15594px;}
	.ft251{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.17551px;}
	.ft252{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.35581px;}
	.ft253{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.19066px;}
	.ft254{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.10217px;}
	.ft255{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.28310px;}
	.ft256{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.28800px;}
	.ft257{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.21177px;}
	.ft258{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.26350px;}
	.ft259{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.12219px;}
	.ft260{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.21508px;}
	.ft261{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.11772px;}
	.ft262{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.51298px;}
	.ft263{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.35413px;}
	.ft264{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.54088px;}
	.ft265{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.19738px;}
	.ft266{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.21177px;}
	.ft267{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.34827px;}
	.ft268{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.32825px;}
	.ft269{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.32989px;}
	.ft270{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.32641px;}
	.ft271{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.18242px;}
	.ft272{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.09331px;}
	.ft273{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.11767px;}
	.ft274{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.31232px;}
	.ft275{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.04850px;}
	.ft276{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.07331px;}
	.ft277{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.19247px;}
	.ft278{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.18046px;}
	.ft279{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.12038px;}
	.ft280{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.03549px;}
	.ft281{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.47044px;}
	.ft282{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.36392px;}
	.ft283{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.33429px;}
	.ft284{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.28908px;}
	.ft285{virtical-align:top;font-size:8px;font-family:Times;color:#000000;font-weight:bold;letter-spacing:1.29082px;}
	.ft286{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.06328px;}
	.ft287{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.03863px;}
	.ft288{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.00356px;}
	.ft289{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.99533px;}
	.ft290{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.99342px;}
	.ft291{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.99944px;}
	.ft292{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.99591px;}
	.ft293{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.99317px;}
	.ft294{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.00261px;}
	.ft295{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.98862px;}
	.ft296{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.98689px;}
	.ft297{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.98198px;}
	.ft298{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.99078px;}
	.ft299{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.98129px;}
	.ft300{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.97993px;}
	.ft301{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.97683px;}
	.ft302{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.98386px;}
	.ft303{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.97657px;}
	.ft304{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:0.98973px;}
	.ft305{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.40183px;}
	.ft306{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.27968px;}
	.ft307{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.20431px;}
	.ft308{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.15783px;}
	.ft309{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.13528px;}
	.ft310{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.12730px;}
	.ft311{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.12007px;}
	.ft312{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.11054px;}
	.ft313{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09948px;}
	.ft314{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09592px;}
	.ft315{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09286px;}
	.ft316{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09570px;}
	.ft317{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09479px;}
	.ft318{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.10027px;}
	.ft319{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09925px;}
	.ft320{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.08965px;}
	.ft321{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.08253px;}
	.ft322{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07849px;}
	.ft323{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07316px;}
	.ft324{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07075px;}
	.ft325{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06819px;}
	.ft326{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06368px;}
	.ft327{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06660px;}
	.ft328{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05950px;}
	.ft329{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05218px;}
	.ft330{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04385px;}
	.ft331{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03978px;}
	.ft332{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04064px;}
	.ft333{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04222px;}
	.ft334{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03987px;}
	.ft335{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03807px;}
	.ft336{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03942px;}
	.ft337{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04078px;}
	.ft338{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.18906px;}
	.ft339{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.12784px;}
	.ft340{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.11613px;}
	.ft341{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09559px;}
	.ft342{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06026px;}
	.ft343{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06045px;}
	.ft344{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04713px;}
	.ft345{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04182px;}
	.ft346{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03962px;}
	.ft347{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02939px;}
	.ft348{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02075px;}
	.ft349{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01753px;}
	.ft350{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02236px;}
	.ft351{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02430px;}
	.ft352{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.02092px;}
	.ft353{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01491px;}
	.ft354{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01326px;}
	.ft355{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.01356px;}
	.ft356{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.00849px;}
	.ft357{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.00561px;}
	.ft358{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.00652px;}
	.ft359{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.00382px;}
	.ft360{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99816px;}
	.ft361{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99723px;}
	.ft362{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99174px;}
	.ft363{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99103px;}
	.ft364{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99036px;}
	.ft365{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99585px;}
	.ft366{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99388px;}
	.ft367{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99440px;}
	.ft368{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99035px;}
	.ft369{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99479px;}
	.ft370{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99306px;}
	.ft371{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99262px;}
	.ft372{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:0.99412px;}
	.ft373{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.26577px;}
	.ft374{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.18023px;}
	.ft375{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.17106px;}
	.ft376{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.14189px;}
	.ft377{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09982px;}
	.ft378{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09460px;}
	.ft379{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.08999px;}
	.ft380{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.09063px;}
	.ft381{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.08134px;}
	.ft382{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07883px;}
	.ft383{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07509px;}
	.ft384{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07972px;}
	.ft385{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07011px;}
	.ft386{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06738px;}
	.ft387{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06764px;}
	.ft388{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06499px;}
	.ft389{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05886px;}
	.ft390{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05965px;}
	.ft391{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05558px;}
	.ft392{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05082px;}
	.ft393{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06156px;}
	.ft394{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05875px;}
	.ft395{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05692px;}
	.ft396{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05552px;}
	.ft397{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05056px;}
	.ft398{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04926px;}
	.ft399{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04716px;}
	.ft400{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04497px;}
	.ft401{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04095px;}
	.ft402{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04023px;}
	.ft403{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03853px;}
	.ft404{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.03707px;}
	.ft405{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.29969px;}
	.ft406{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.17050px;}
	.ft407{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.13523px;}
	.ft408{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.08527px;}
	.ft409{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07104px;}
	.ft410{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07649px;}
	.ft411{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06831px;}
	.ft412{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06273px;}
	.ft413{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07445px;}
	.ft414{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07010px;}
	.ft415{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07036px;}
	.ft416{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07014px;}
	.ft417{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06282px;}
	.ft418{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06373px;}
	.ft419{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07405px;}
	.ft420{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07393px;}
	.ft421{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.07132px;}
	.ft422{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06254px;}
	.ft423{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05935px;}
	.ft424{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06140px;}
	.ft425{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05819px;}
	.ft426{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05943px;}
	.ft427{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05984px;}
	.ft428{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06042px;}
	.ft429{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.06058px;}
	.ft430{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05769px;}
	.ft431{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05543px;}
	.ft432{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05434px;}
	.ft433{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05575px;}
	.ft434{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.05365px;}
	.ft435{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04977px;}
	.ft436{virtical-align:top;font-size:6px;font-family:Times;color:#000000;letter-spacing:1.04538px;}
	.ft437{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.60256px;}
	.ft438{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.26975px;}
	.ft439{virtical-align:top;font-size:8px;font-family:Times;color:#000000;letter-spacing:1.18183px;}
-->
</STYLE>
</HEAD>
<BODY bgcolor="#A0A0A0" vlink="blue" link="blue">
<IMG width="918" height="1188" src="20180630001.png" alt="background image">
<DIV style="position:absolute;top:46;left:75"><nobr><span class="ft22">TCM Group A/S Ordinary Shares TCM</span></nobr></DIV>
<DIV style="position:absolute;top:85;left:75"><nobr><span class="ft23">Last Close</span></nobr></DIV>
<DIV style="position:absolute;top:85;left:214"><nobr><span class="ft25">Fair Value</span><span class="ft3">Q</span></nobr></DIV>
<DIV style="position:absolute;top:85;left:392"><nobr><span class="ft26">Market Cap</span></nobr></DIV>
<DIV style="position:absolute;top:85;left:543"><nobr><span class="ft4">Sector</span></nobr></DIV>
<DIV style="position:absolute;top:85;left:659"><nobr><span class="ft4">Industry</span></nobr></DIV>
<DIV style="position:absolute;top:85;left:762"><nobr><span class="ft28">Country of Domicile</span></nobr></DIV>
<DIV style="position:absolute;top:98;left:75"><nobr><span class="ft30">31 Aug 2018</span></nobr></DIV>
<DIV style="position:absolute;top:98;left:214"><nobr><span class="ft34">03 Sep 2018 02:00 UTC</span></nobr></DIV>
<DIV style="position:absolute;top:98;left:392"><nobr><span class="ft36">31 Aug 2018</span></nobr></DIV>
<DIV style="position:absolute;top:109;left:75"><nobr><span class="ft6">110.00</span></nobr></DIV>
<DIV style="position:absolute;top:109;left:214"><nobr><span class="ft6">102.68</span></nobr></DIV>
<DIV style="position:absolute;top:109;left:392"><nobr><span class="ft37">1,100.0 Mil</span></nobr></DIV>
<DIV style="position:absolute;top:107;left:543"><nobr><span class="ft39">t </span><span class="ft8">Consumer Cyclical</span></nobr></DIV>
<DIV style="position:absolute;top:112;left:659"><nobr><span class="ft44">Home Furnishings &amp; Fixtures </span><span class="ft9">DNK </span><span class="ft8">Denmark</span></nobr></DIV>
<DIV style="position:absolute;top:136;left:75"><nobr><span class="ft57">There is no one analyst in which a Quantitative Fair Value Estimate and Quantitative</span></nobr></DIV>
<DIV style="position:absolute;top:146;left:75"><nobr><span class="ft68">Star Rating are attributed to; however, Mr. Lee Davidson, Head of Quantitative</span></nobr></DIV>
<DIV style="position:absolute;top:157;left:75"><nobr><span class="ft78">Research for Morningstar, Inc., is responsible for overseeing the methodology that</span></nobr></DIV>
<DIV style="position:absolute;top:167;left:75"><nobr><span class="ft89">supports the quantitative fair value. As an employee of Morningstar, Inc., Mr.</span></nobr></DIV>
<DIV style="position:absolute;top:178;left:75"><nobr><span class="ft100">Davidson is guided by Morningstar, Inc.'s Code of Ethics and Personal Securities</span></nobr></DIV>
<DIV style="position:absolute;top:188;left:75"><nobr><span class="ft110">Trading Policy in carrying out his responsibilities. For information regarding Conflicts</span></nobr></DIV>
<DIV style="position:absolute;top:199;left:75"><nobr><span class="ft113">of Interests, visit http://global.morningstar.com/equitydisclosures</span></nobr></DIV>
<DIV style="position:absolute;top:233;left:75"><nobr><span class="ft114">Company Profile</span></nobr></DIV>
<DIV style="position:absolute;top:248;left:75"><nobr><span class="ft121">TCM Group A/S manufactures and supplies kitchen and</span></nobr></DIV>
<DIV style="position:absolute;top:263;left:75"><nobr><span class="ft129">furniture products for bathrooms and storage in Denmark and</span></nobr></DIV>
<DIV style="position:absolute;top:278;left:75"><nobr><span class="ft135">the other Scandinavian countries. Its products include</span></nobr></DIV>
<DIV style="position:absolute;top:293;left:75"><nobr><span class="ft142">drawers, cabinets, fronts, table tops, handles, and other</span></nobr></DIV>
<DIV style="position:absolute;top:308;left:75"><nobr><span class="ft150">accessories. It offers its products under the Svane Kokkenet,</span></nobr></DIV>
<DIV style="position:absolute;top:323;left:75"><nobr><span class="ft157">Tvis Kokkener, Nettoline, and kitchen brands. The company</span></nobr></DIV>
<DIV style="position:absolute;top:338;left:75"><nobr><span class="ft164">also sells private label products through Do-It-Yourself and</span></nobr></DIV>
<DIV style="position:absolute;top:353;left:75"><nobr><span class="ft170">kitchen specialty stores in Denmark and Norway.</span></nobr></DIV>
<DIV style="position:absolute;top:398;left:75"><nobr><span class="ft171">Quantitative Scores</span></nobr></DIV>
<DIV style="position:absolute;top:398;left:223"><nobr><span class="ft8">Scores</span></nobr></DIV>
<DIV style="position:absolute;top:413;left:232"><nobr><span class="ft175">All Rel Sector Rel Country</span></nobr></DIV>
<DIV style="position:absolute;top:427;left:75"><nobr><span class="ft176">Quantitative Moat</span></nobr></DIV>
<DIV style="position:absolute;top:427;left:170"><nobr><span class="ft12">None</span></nobr></DIV>
<DIV style="position:absolute;top:427;left:232"><nobr><span class="ft12">56</span></nobr></DIV>
<DIV style="position:absolute;top:427;left:273"><nobr><span class="ft12">57</span></nobr></DIV>
<DIV style="position:absolute;top:427;left:320"><nobr><span class="ft12">44</span></nobr></DIV>
<DIV style="position:absolute;top:442;left:75"><nobr><span class="ft12">Valuation</span></nobr></DIV>
<DIV style="position:absolute;top:442;left:170"><nobr><span class="ft12">Overvalued</span></nobr></DIV>
<DIV style="position:absolute;top:442;left:232"><nobr><span class="ft12">11</span></nobr></DIV>
<DIV style="position:absolute;top:442;left:273"><nobr><span class="ft12">10</span></nobr></DIV>
<DIV style="position:absolute;top:442;left:320"><nobr><span class="ft12">24</span></nobr></DIV>
<DIV style="position:absolute;top:457;left:75"><nobr><span class="ft178">Quantitative Uncertainty High</span></nobr></DIV>
<DIV style="position:absolute;top:457;left:232"><nobr><span class="ft12">92</span></nobr></DIV>
<DIV style="position:absolute;top:457;left:273"><nobr><span class="ft12">92</span></nobr></DIV>
<DIV style="position:absolute;top:457;left:320"><nobr><span class="ft12">82</span></nobr></DIV>
<DIV style="position:absolute;top:472;left:75"><nobr><span class="ft179">Financial Health</span></nobr></DIV>
<DIV style="position:absolute;top:472;left:170"><nobr><span class="ft12">Moderate</span></nobr></DIV>
<DIV style="position:absolute;top:472;left:232"><nobr><span class="ft12">73</span></nobr></DIV>
<DIV style="position:absolute;top:472;left:273"><nobr><span class="ft12">63</span></nobr></DIV>
<DIV style="position:absolute;top:472;left:320"><nobr><span class="ft12">46</span></nobr></DIV>
<DIV style="position:absolute;top:567;left:75"><nobr><span class="ft182">Source: Morningstar Equity Research</span></nobr></DIV>
<DIV style="position:absolute;top:518;left:140"><nobr><span class="ft13">t</span></nobr></DIV>
<DIV style="position:absolute;top:520;left:162"><nobr><span class="ft14">DNK</span></nobr></DIV>
<DIV style="position:absolute;top:504;left:243"><nobr><span class="ft8">TCM</span></nobr></DIV>
<DIV style="position:absolute;top:544;left:77"><nobr><span class="ft8">Undervalued</span></nobr></DIV>
<DIV style="position:absolute;top:544;left:161"><nobr><span class="ft183">Fairly Valued</span></nobr></DIV>
<DIV style="position:absolute;top:544;left:291"><nobr><span class="ft8">Overvalued</span></nobr></DIV>
<DIV style="position:absolute;top:601;left:75"><nobr><span class="ft4">Valuation</span></nobr></DIV>
<DIV style="position:absolute;top:611;left:178"><nobr><span class="ft185">Current 5-Yr Avg</span></nobr></DIV>
<DIV style="position:absolute;top:601;left:261"><nobr><span class="ft8">Sector</span></nobr></DIV>
<DIV style="position:absolute;top:611;left:257"><nobr><span class="ft8">Median</span></nobr></DIV>
<DIV style="position:absolute;top:601;left:303"><nobr><span class="ft8">Country</span></nobr></DIV>
<DIV style="position:absolute;top:611;left:303"><nobr><span class="ft8">Median</span></nobr></DIV>
<DIV style="position:absolute;top:627;left:75"><nobr><span class="ft187">Price/Quant Fair Value</span></nobr></DIV>
<DIV style="position:absolute;top:627;left:187"><nobr><span class="ft12">1.07</span></nobr></DIV>
<DIV style="position:absolute;top:627;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:627;left:267"><nobr><span class="ft12">0.91</span></nobr></DIV>
<DIV style="position:absolute;top:627;left:313"><nobr><span class="ft12">0.97</span></nobr></DIV>
<DIV style="position:absolute;top:642;left:75"><nobr><span class="ft12">Price/Earnings</span></nobr></DIV>
<DIV style="position:absolute;top:642;left:187"><nobr><span class="ft12">24.4</span></nobr></DIV>
<DIV style="position:absolute;top:642;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:642;left:267"><nobr><span class="ft12">17.5</span></nobr></DIV>
<DIV style="position:absolute;top:642;left:313"><nobr><span class="ft12">19.8</span></nobr></DIV>
<DIV style="position:absolute;top:657;left:75"><nobr><span class="ft188">Forward P/E</span></nobr></DIV>
<DIV style="position:absolute;top:657;left:193"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:657;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:657;left:267"><nobr><span class="ft12">14.4</span></nobr></DIV>
<DIV style="position:absolute;top:657;left:313"><nobr><span class="ft12">22.0</span></nobr></DIV>
<DIV style="position:absolute;top:672;left:75"><nobr><span class="ft189">Price/Cash Flow</span></nobr></DIV>
<DIV style="position:absolute;top:672;left:187"><nobr><span class="ft12">10.9</span></nobr></DIV>
<DIV style="position:absolute;top:672;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:672;left:267"><nobr><span class="ft12">10.9</span></nobr></DIV>
<DIV style="position:absolute;top:672;left:313"><nobr><span class="ft12">17.4</span></nobr></DIV>
<DIV style="position:absolute;top:687;left:75"><nobr><span class="ft191">Price/Free Cash Flow</span></nobr></DIV>
<DIV style="position:absolute;top:687;left:187"><nobr><span class="ft12">11.8</span></nobr></DIV>
<DIV style="position:absolute;top:687;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:687;left:267"><nobr><span class="ft12">18.9</span></nobr></DIV>
<DIV style="position:absolute;top:687;left:313"><nobr><span class="ft12">23.0</span></nobr></DIV>
<DIV style="position:absolute;top:702;left:75"><nobr><span class="ft194">Trailing Dividend Yield %</span></nobr></DIV>
<DIV style="position:absolute;top:702;left:193"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:702;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:702;left:267"><nobr><span class="ft12">2.26</span></nobr></DIV>
<DIV style="position:absolute;top:702;left:313"><nobr><span class="ft12">2.15</span></nobr></DIV>
<DIV style="position:absolute;top:717;left:75"><nobr><span class="ft12">Price/Book</span></nobr></DIV>
<DIV style="position:absolute;top:717;left:192"><nobr><span class="ft12">3.6</span></nobr></DIV>
<DIV style="position:absolute;top:717;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:717;left:272"><nobr><span class="ft12">1.8</span></nobr></DIV>
<DIV style="position:absolute;top:717;left:318"><nobr><span class="ft12">2.9</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:75"><nobr><span class="ft12">Price/Sales</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:192"><nobr><span class="ft12">1.4</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:272"><nobr><span class="ft12">1.0</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:318"><nobr><span class="ft12">2.0</span></nobr></DIV>
<DIV style="position:absolute;top:764;left:75"><nobr><span class="ft4">Profitability</span></nobr></DIV>
<DIV style="position:absolute;top:774;left:178"><nobr><span class="ft185">Current 5-Yr Avg</span></nobr></DIV>
<DIV style="position:absolute;top:764;left:261"><nobr><span class="ft8">Sector</span></nobr></DIV>
<DIV style="position:absolute;top:774;left:257"><nobr><span class="ft8">Median</span></nobr></DIV>
<DIV style="position:absolute;top:764;left:303"><nobr><span class="ft8">Country</span></nobr></DIV>
<DIV style="position:absolute;top:774;left:303"><nobr><span class="ft8">Median</span></nobr></DIV>
<DIV style="position:absolute;top:790;left:75"><nobr><span class="ft197">Return on Equity %</span></nobr></DIV>
<DIV style="position:absolute;top:790;left:187"><nobr><span class="ft12">14.9</span></nobr></DIV>
<DIV style="position:absolute;top:790;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:790;left:267"><nobr><span class="ft12">12.0</span></nobr></DIV>
<DIV style="position:absolute;top:790;left:313"><nobr><span class="ft12">14.3</span></nobr></DIV>
<DIV style="position:absolute;top:804;left:75"><nobr><span class="ft199">Return on Assets %</span></nobr></DIV>
<DIV style="position:absolute;top:804;left:192"><nobr><span class="ft12">6.0</span></nobr></DIV>
<DIV style="position:absolute;top:804;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:804;left:272"><nobr><span class="ft12">5.4</span></nobr></DIV>
<DIV style="position:absolute;top:804;left:318"><nobr><span class="ft12">6.6</span></nobr></DIV>
<DIV style="position:absolute;top:819;left:75"><nobr><span class="ft200">Revenue/Employee (Mil)</span></nobr></DIV>
<DIV style="position:absolute;top:819;left:192"><nobr><span class="ft12">1.8</span></nobr></DIV>
<DIV style="position:absolute;top:819;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:819;left:272"><nobr><span class="ft12">0.6</span></nobr></DIV>
<DIV style="position:absolute;top:819;left:318"><nobr><span class="ft12">1.6</span></nobr></DIV>
<DIV style="position:absolute;top:849;left:75"><nobr><span class="ft201">Financial Health</span></nobr></DIV>
<DIV style="position:absolute;top:860;left:178"><nobr><span class="ft185">Current 5-Yr Avg</span></nobr></DIV>
<DIV style="position:absolute;top:850;left:261"><nobr><span class="ft8">Sector</span></nobr></DIV>
<DIV style="position:absolute;top:860;left:257"><nobr><span class="ft8">Median</span></nobr></DIV>
<DIV style="position:absolute;top:850;left:303"><nobr><span class="ft8">Country</span></nobr></DIV>
<DIV style="position:absolute;top:860;left:303"><nobr><span class="ft8">Median</span></nobr></DIV>
<DIV style="position:absolute;top:876;left:75"><nobr><span class="ft203">Distance to Default</span></nobr></DIV>
<DIV style="position:absolute;top:876;left:192"><nobr><span class="ft12">0.7</span></nobr></DIV>
<DIV style="position:absolute;top:876;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:876;left:272"><nobr><span class="ft12">0.6</span></nobr></DIV>
<DIV style="position:absolute;top:876;left:318"><nobr><span class="ft12">0.7</span></nobr></DIV>
<DIV style="position:absolute;top:891;left:75"><nobr><span class="ft204">Solvency Score</span></nobr></DIV>
<DIV style="position:absolute;top:891;left:183"><nobr><span class="ft12">530.2</span></nobr></DIV>
<DIV style="position:absolute;top:891;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:891;left:263"><nobr><span class="ft12">485.9</span></nobr></DIV>
<DIV style="position:absolute;top:891;left:309"><nobr><span class="ft12">501.8</span></nobr></DIV>
<DIV style="position:absolute;top:905;left:75"><nobr><span class="ft12">Assets/Equity</span></nobr></DIV>
<DIV style="position:absolute;top:905;left:192"><nobr><span class="ft12">2.6</span></nobr></DIV>
<DIV style="position:absolute;top:905;left:230"><nobr><span class="ft12">2.4</span></nobr></DIV>
<DIV style="position:absolute;top:905;left:272"><nobr><span class="ft12">1.8</span></nobr></DIV>
<DIV style="position:absolute;top:905;left:318"><nobr><span class="ft12">2.3</span></nobr></DIV>
<DIV style="position:absolute;top:920;left:75"><nobr><span class="ft205">Long-Term Debt/Equity</span></nobr></DIV>
<DIV style="position:absolute;top:920;left:192"><nobr><span class="ft12">0.8</span></nobr></DIV>
<DIV style="position:absolute;top:920;left:231"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:920;left:272"><nobr><span class="ft12">0.2</span></nobr></DIV>
<DIV style="position:absolute;top:920;left:318"><nobr><span class="ft12">0.2</span></nobr></DIV>
<DIV style="position:absolute;top:140;left:347"><nobr><span class="ft209">Price vs. Quantitative Fair Value</span></nobr></DIV>
<DIV style="position:absolute;top:319;left:706"><nobr><span class="ft8">34</span></nobr></DIV>
<DIV style="position:absolute;top:287;left:706"><nobr><span class="ft8">68</span></nobr></DIV>
<DIV style="position:absolute;top:255;left:702"><nobr><span class="ft8">102</span></nobr></DIV>
<DIV style="position:absolute;top:223;left:702"><nobr><span class="ft8">136</span></nobr></DIV>
<DIV style="position:absolute;top:191;left:702"><nobr><span class="ft8">170</span></nobr></DIV>
<DIV style="position:absolute;top:156;left:370"><nobr><span class="ft4">2014</span></nobr></DIV>
<DIV style="position:absolute;top:156;left:431"><nobr><span class="ft4">2015</span></nobr></DIV>
<DIV style="position:absolute;top:156;left:493"><nobr><span class="ft4">2016</span></nobr></DIV>
<DIV style="position:absolute;top:156;left:554"><nobr><span class="ft4">2017</span></nobr></DIV>
<DIV style="position:absolute;top:156;left:615"><nobr><span class="ft4">2018</span></nobr></DIV>
<DIV style="position:absolute;top:156;left:676"><nobr><span class="ft4">2019</span></nobr></DIV>
<DIV style="position:absolute;top:156;left:746"><nobr><span class="ft212">Quantitative Fair Value Estimate</span></nobr></DIV>
<DIV style="position:absolute;top:169;left:746"><nobr><span class="ft213">Total Return</span></nobr></DIV>
<DIV style="position:absolute;top:184;left:746"><nobr><span class="ft12">Sales/Share</span></nobr></DIV>
<DIV style="position:absolute;top:198;left:746"><nobr><span class="ft214">Forecast Range</span></nobr></DIV>
<DIV style="position:absolute;top:211;left:746"><nobr><span class="ft215">Forcasted Price</span></nobr></DIV>
<DIV style="position:absolute;top:225;left:746"><nobr><span class="ft12">Dividend</span></nobr></DIV>
<DIV style="position:absolute;top:238;left:746"><nobr><span class="ft12">Split</span></nobr></DIV>
<DIV style="position:absolute;top:252;left:730"><nobr><span class="ft12">Momentum:</span></nobr></DIV>
<DIV style="position:absolute;top:252;left:815"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:265;left:730"><nobr><span class="ft217">Standard Deviation: --</span></nobr></DIV>
<DIV style="position:absolute;top:279;left:730"><nobr><span class="ft12">Liquidity:</span></nobr></DIV>
<DIV style="position:absolute;top:279;left:815"><nobr><span class="ft12">Medium</span></nobr></DIV>
<DIV style="position:absolute;top:362;left:384"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:362;left:445"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:362;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:362;left:568"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:362;left:623"><nobr><span class="ft12">11.7</span></nobr></DIV>
<DIV style="position:absolute;top:362;left:728"><nobr><span class="ft218">Total Return %</span></nobr></DIV>
<DIV style="position:absolute;top:377;left:384"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:377;left:445"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:377;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:377;left:568"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:377;left:623"><nobr><span class="ft12">14.8</span></nobr></DIV>
<DIV style="position:absolute;top:377;left:728"><nobr><span class="ft221">+/­ Market (Morningstar World</span></nobr></DIV>
<DIV style="position:absolute;top:388;left:728"><nobr><span class="ft12">Index)</span></nobr></DIV>
<DIV style="position:absolute;top:395;left:384"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:395;left:445"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:395;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:395;left:568"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:395;left:629"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:395;left:728"><nobr><span class="ft224">Trailing Dividend Yield %</span></nobr></DIV>
<DIV style="position:absolute;top:410;left:384"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:410;left:445"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:410;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:410;left:568"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:410;left:629"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:410;left:728"><nobr><span class="ft227">Forward Dividend Yield %</span></nobr></DIV>
<DIV style="position:absolute;top:425;left:384"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:425;left:445"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:425;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:425;left:568"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:425;left:623"><nobr><span class="ft12">24.4</span></nobr></DIV>
<DIV style="position:absolute;top:425;left:728"><nobr><span class="ft12">Price/Earnings</span></nobr></DIV>
<DIV style="position:absolute;top:440;left:384"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:440;left:445"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:440;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:440;left:568"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:440;left:628"><nobr><span class="ft12">1.4</span></nobr></DIV>
<DIV style="position:absolute;top:440;left:728"><nobr><span class="ft12">Price/Revenue</span></nobr></DIV>
<DIV style="position:absolute;top:461;left:728"><nobr><span class="ft229">Morningstar Rating</span><span class="ft15">Q</span></nobr></DIV>
<DIV style="position:absolute;top:514;left:729"><nobr><span class="ft8">Q</span></nobr></DIV>
<DIV style="position:absolute;top:503;left:729"><nobr><span class="ft8">QQ</span></nobr></DIV>
<DIV style="position:absolute;top:492;left:729"><nobr><span class="ft8">QQQ</span></nobr></DIV>
<DIV style="position:absolute;top:481;left:729"><nobr><span class="ft8">QQQQ</span></nobr></DIV>
<DIV style="position:absolute;top:470;left:729"><nobr><span class="ft8">QQQQQ</span></nobr></DIV>
<DIV style="position:absolute;top:538;left:377"><nobr><span class="ft4">2013</span></nobr></DIV>
<DIV style="position:absolute;top:538;left:439"><nobr><span class="ft4">2014</span></nobr></DIV>
<DIV style="position:absolute;top:538;left:500"><nobr><span class="ft4">2015</span></nobr></DIV>
<DIV style="position:absolute;top:538;left:561"><nobr><span class="ft4">2016</span></nobr></DIV>
<DIV style="position:absolute;top:538;left:623"><nobr><span class="ft4">2017</span></nobr></DIV>
<DIV style="position:absolute;top:538;left:683"><nobr><span class="ft4">TTM</span></nobr></DIV>
<DIV style="position:absolute;top:538;left:721"><nobr><span class="ft233">Financials (Fiscal Year in K)</span></nobr></DIV>
<DIV style="position:absolute;top:549;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:549;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:549;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:549;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:549;left:608"><nobr><span class="ft12">817,330</span></nobr></DIV>
<DIV style="position:absolute;top:549;left:670"><nobr><span class="ft12">817,330</span></nobr></DIV>
<DIV style="position:absolute;top:549;left:721"><nobr><span class="ft12">Revenue</span></nobr></DIV>
<DIV style="position:absolute;top:564;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:564;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:564;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:564;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:564;left:628"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:564;left:688"><nobr><span class="ft12">0.0</span></nobr></DIV>
<DIV style="position:absolute;top:564;left:723"><nobr><span class="ft234">% Change</span></nobr></DIV>
<DIV style="position:absolute;top:579;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:579;left:429"><nobr><span class="ft12">70,500</span></nobr></DIV>
<DIV style="position:absolute;top:579;left:486"><nobr><span class="ft12">102,300</span></nobr></DIV>
<DIV style="position:absolute;top:579;left:547"><nobr><span class="ft12">139,900</span></nobr></DIV>
<DIV style="position:absolute;top:579;left:608"><nobr><span class="ft12">115,193</span></nobr></DIV>
<DIV style="position:absolute;top:579;left:670"><nobr><span class="ft12">115,193</span></nobr></DIV>
<DIV style="position:absolute;top:579;left:721"><nobr><span class="ft235">Operating Income</span></nobr></DIV>
<DIV style="position:absolute;top:594;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:594;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:594;left:500"><nobr><span class="ft12">45.1</span></nobr></DIV>
<DIV style="position:absolute;top:594;left:561"><nobr><span class="ft12">36.8</span></nobr></DIV>
<DIV style="position:absolute;top:594;left:619"><nobr><span class="ft12">-17.7</span></nobr></DIV>
<DIV style="position:absolute;top:594;left:688"><nobr><span class="ft12">0.0</span></nobr></DIV>
<DIV style="position:absolute;top:594;left:723"><nobr><span class="ft234">% Change</span></nobr></DIV>
<DIV style="position:absolute;top:609;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:609;left:429"><nobr><span class="ft12">24,100</span></nobr></DIV>
<DIV style="position:absolute;top:609;left:490"><nobr><span class="ft12">48,200</span></nobr></DIV>
<DIV style="position:absolute;top:609;left:552"><nobr><span class="ft12">31,700</span></nobr></DIV>
<DIV style="position:absolute;top:609;left:613"><nobr><span class="ft12">47,993</span></nobr></DIV>
<DIV style="position:absolute;top:609;left:674"><nobr><span class="ft12">47,993</span></nobr></DIV>
<DIV style="position:absolute;top:609;left:721"><nobr><span class="ft236">Net Income</span></nobr></DIV>
<DIV style="position:absolute;top:625;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:625;left:429"><nobr><span class="ft12">57,200</span></nobr></DIV>
<DIV style="position:absolute;top:625;left:490"><nobr><span class="ft12">91,200</span></nobr></DIV>
<DIV style="position:absolute;top:625;left:552"><nobr><span class="ft12">80,300</span></nobr></DIV>
<DIV style="position:absolute;top:625;left:608"><nobr><span class="ft12">107,471</span></nobr></DIV>
<DIV style="position:absolute;top:625;left:670"><nobr><span class="ft12">107,471</span></nobr></DIV>
<DIV style="position:absolute;top:625;left:721"><nobr><span class="ft238">Operating Cash Flow</span></nobr></DIV>
<DIV style="position:absolute;top:640;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:640;left:431"><nobr><span class="ft12">-6,100</span></nobr></DIV>
<DIV style="position:absolute;top:640;left:492"><nobr><span class="ft12">-5,400</span></nobr></DIV>
<DIV style="position:absolute;top:640;left:553"><nobr><span class="ft12">-4,400</span></nobr></DIV>
<DIV style="position:absolute;top:640;left:615"><nobr><span class="ft12">-8,418</span></nobr></DIV>
<DIV style="position:absolute;top:640;left:676"><nobr><span class="ft12">-8,418</span></nobr></DIV>
<DIV style="position:absolute;top:640;left:721"><nobr><span class="ft239">Capital Spending</span></nobr></DIV>
<DIV style="position:absolute;top:655;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:655;left:429"><nobr><span class="ft12">51,100</span></nobr></DIV>
<DIV style="position:absolute;top:655;left:490"><nobr><span class="ft12">85,800</span></nobr></DIV>
<DIV style="position:absolute;top:655;left:552"><nobr><span class="ft12">75,900</span></nobr></DIV>
<DIV style="position:absolute;top:655;left:613"><nobr><span class="ft12">99,053</span></nobr></DIV>
<DIV style="position:absolute;top:655;left:674"><nobr><span class="ft12">99,053</span></nobr></DIV>
<DIV style="position:absolute;top:655;left:721"><nobr><span class="ft241">Free Cash Flow</span></nobr></DIV>
<DIV style="position:absolute;top:670;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:670;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:670;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:670;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:670;left:622"><nobr><span class="ft12">12.1</span></nobr></DIV>
<DIV style="position:absolute;top:670;left:684"><nobr><span class="ft12">12.1</span></nobr></DIV>
<DIV style="position:absolute;top:670;left:723"><nobr><span class="ft242">% Sales</span></nobr></DIV>
<DIV style="position:absolute;top:686;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:686;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:686;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:686;left:561"><nobr><span class="ft12">3.17</span></nobr></DIV>
<DIV style="position:absolute;top:686;left:622"><nobr><span class="ft12">4.51</span></nobr></DIV>
<DIV style="position:absolute;top:686;left:684"><nobr><span class="ft12">4.51</span></nobr></DIV>
<DIV style="position:absolute;top:686;left:721"><nobr><span class="ft12">EPS</span></nobr></DIV>
<DIV style="position:absolute;top:701;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:701;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:701;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:701;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:701;left:622"><nobr><span class="ft12">42.3</span></nobr></DIV>
<DIV style="position:absolute;top:701;left:688"><nobr><span class="ft12">0.0</span></nobr></DIV>
<DIV style="position:absolute;top:701;left:723"><nobr><span class="ft234">% Change</span></nobr></DIV>
<DIV style="position:absolute;top:716;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:716;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:716;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:716;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:716;left:618"><nobr><span class="ft12">11.33</span></nobr></DIV>
<DIV style="position:absolute;top:716;left:684"><nobr><span class="ft12">9.30</span></nobr></DIV>
<DIV style="position:absolute;top:716;left:721"><nobr><span class="ft243">Free Cash Flow/Share</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:628"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:689"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:732;left:721"><nobr><span class="ft12">Dividends/Share</span></nobr></DIV>
<DIV style="position:absolute;top:747;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:747;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:747;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:747;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:747;left:618"><nobr><span class="ft12">37.83</span></nobr></DIV>
<DIV style="position:absolute;top:747;left:679"><nobr><span class="ft12">30.48</span></nobr></DIV>
<DIV style="position:absolute;top:747;left:721"><nobr><span class="ft244">Book Value/Share</span></nobr></DIV>
<DIV style="position:absolute;top:762;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:762;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:762;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:762;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:762;left:613"><nobr><span class="ft12">10,000</span></nobr></DIV>
<DIV style="position:absolute;top:762;left:674"><nobr><span class="ft12">10,000</span></nobr></DIV>
<DIV style="position:absolute;top:762;left:721"><nobr><span class="ft246">Shares Outstanding (K)</span></nobr></DIV>
<DIV style="position:absolute;top:787;left:721"><nobr><span class="ft2">Profitability</span></nobr></DIV>
<DIV style="position:absolute;top:798;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:798;left:438"><nobr><span class="ft12">17.8</span></nobr></DIV>
<DIV style="position:absolute;top:798;left:500"><nobr><span class="ft12">30.2</span></nobr></DIV>
<DIV style="position:absolute;top:798;left:561"><nobr><span class="ft12">12.1</span></nobr></DIV>
<DIV style="position:absolute;top:798;left:622"><nobr><span class="ft12">14.9</span></nobr></DIV>
<DIV style="position:absolute;top:798;left:684"><nobr><span class="ft12">14.9</span></nobr></DIV>
<DIV style="position:absolute;top:798;left:721"><nobr><span class="ft249">Return on Equity %</span></nobr></DIV>
<DIV style="position:absolute;top:813;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:813;left:443"><nobr><span class="ft12">7.4</span></nobr></DIV>
<DIV style="position:absolute;top:813;left:500"><nobr><span class="ft12">13.8</span></nobr></DIV>
<DIV style="position:absolute;top:813;left:566"><nobr><span class="ft12">5.4</span></nobr></DIV>
<DIV style="position:absolute;top:813;left:627"><nobr><span class="ft12">6.0</span></nobr></DIV>
<DIV style="position:absolute;top:813;left:688"><nobr><span class="ft12">6.0</span></nobr></DIV>
<DIV style="position:absolute;top:813;left:721"><nobr><span class="ft251">Return on Assets %</span></nobr></DIV>
<DIV style="position:absolute;top:828;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:828;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:828;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:828;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:828;left:627"><nobr><span class="ft12">5.9</span></nobr></DIV>
<DIV style="position:absolute;top:828;left:688"><nobr><span class="ft12">5.9</span></nobr></DIV>
<DIV style="position:absolute;top:828;left:721"><nobr><span class="ft252">Net Margin %</span></nobr></DIV>
<DIV style="position:absolute;top:843;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:843;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:843;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:843;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:843;left:622"><nobr><span class="ft12">1.02</span></nobr></DIV>
<DIV style="position:absolute;top:843;left:684"><nobr><span class="ft12">1.02</span></nobr></DIV>
<DIV style="position:absolute;top:843;left:721"><nobr><span class="ft253">Asset Turnover</span></nobr></DIV>
<DIV style="position:absolute;top:858;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:858;left:443"><nobr><span class="ft12">2.4</span></nobr></DIV>
<DIV style="position:absolute;top:858;left:504"><nobr><span class="ft12">2.0</span></nobr></DIV>
<DIV style="position:absolute;top:858;left:566"><nobr><span class="ft12">2.3</span></nobr></DIV>
<DIV style="position:absolute;top:858;left:627"><nobr><span class="ft12">2.6</span></nobr></DIV>
<DIV style="position:absolute;top:858;left:688"><nobr><span class="ft12">2.6</span></nobr></DIV>
<DIV style="position:absolute;top:858;left:721"><nobr><span class="ft254">Financial Leverage</span></nobr></DIV>
<DIV style="position:absolute;top:874;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:874;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:874;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:874;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:874;left:622"><nobr><span class="ft12">28.3</span></nobr></DIV>
<DIV style="position:absolute;top:874;left:684"><nobr><span class="ft12">28.3</span></nobr></DIV>
<DIV style="position:absolute;top:874;left:721"><nobr><span class="ft256">Gross Margin %</span></nobr></DIV>
<DIV style="position:absolute;top:889;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:889;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:889;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:889;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:889;left:622"><nobr><span class="ft12">14.1</span></nobr></DIV>
<DIV style="position:absolute;top:889;left:684"><nobr><span class="ft12">14.1</span></nobr></DIV>
<DIV style="position:absolute;top:889;left:721"><nobr><span class="ft257">Operating Margin %</span></nobr></DIV>
<DIV style="position:absolute;top:904;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:904;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:904;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:904;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:904;left:608"><nobr><span class="ft12">235,161</span></nobr></DIV>
<DIV style="position:absolute;top:904;left:670"><nobr><span class="ft12">235,161</span></nobr></DIV>
<DIV style="position:absolute;top:904;left:721"><nobr><span class="ft258">Long-Term Debt</span></nobr></DIV>
<DIV style="position:absolute;top:919;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:919;left:424"><nobr><span class="ft12">135,400</span></nobr></DIV>
<DIV style="position:absolute;top:919;left:486"><nobr><span class="ft12">183,700</span></nobr></DIV>
<DIV style="position:absolute;top:919;left:547"><nobr><span class="ft12">339,900</span></nobr></DIV>
<DIV style="position:absolute;top:919;left:608"><nobr><span class="ft12">304,777</span></nobr></DIV>
<DIV style="position:absolute;top:919;left:670"><nobr><span class="ft12">304,777</span></nobr></DIV>
<DIV style="position:absolute;top:919;left:721"><nobr><span class="ft259">Total Equity</span></nobr></DIV>
<DIV style="position:absolute;top:934;left:383"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:934;left:444"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:934;left:506"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:934;left:567"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:934;left:627"><nobr><span class="ft12">8.5</span></nobr></DIV>
<DIV style="position:absolute;top:934;left:688"><nobr><span class="ft12">8.5</span></nobr></DIV>
<DIV style="position:absolute;top:934;left:721"><nobr><span class="ft261">Fixed Asset Turns</span></nobr></DIV>
<DIV style="position:absolute;top:953;left:75"><nobr><span class="ft263">Growth Per Share</span></nobr></DIV>
<DIV style="position:absolute;top:965;left:185"><nobr><span class="ft8">1-Year</span></nobr></DIV>
<DIV style="position:absolute;top:965;left:226"><nobr><span class="ft8">3-Year</span></nobr></DIV>
<DIV style="position:absolute;top:965;left:268"><nobr><span class="ft8">5-Year</span></nobr></DIV>
<DIV style="position:absolute;top:965;left:302"><nobr><span class="ft8">10-Year</span></nobr></DIV>
<DIV style="position:absolute;top:980;left:75"><nobr><span class="ft264">Revenue %</span></nobr></DIV>
<DIV style="position:absolute;top:980;left:192"><nobr><span class="ft12">60.7</span></nobr></DIV>
<DIV style="position:absolute;top:980;left:239"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:980;left:281"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:980;left:319"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:995;left:75"><nobr><span class="ft266">Operating Income %</span></nobr></DIV>
<DIV style="position:absolute;top:995;left:192"><nobr><span class="ft12">58.0</span></nobr></DIV>
<DIV style="position:absolute;top:995;left:233"><nobr><span class="ft12">17.8</span></nobr></DIV>
<DIV style="position:absolute;top:995;left:281"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:995;left:319"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1010;left:75"><nobr><span class="ft267">Earnings %</span></nobr></DIV>
<DIV style="position:absolute;top:1010;left:192"><nobr><span class="ft12">42.3</span></nobr></DIV>
<DIV style="position:absolute;top:1010;left:239"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1010;left:281"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1010;left:319"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1025;left:75"><nobr><span class="ft268">Dividends %</span></nobr></DIV>
<DIV style="position:absolute;top:1025;left:198"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1025;left:239"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1025;left:281"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1025;left:319"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1040;left:75"><nobr><span class="ft270">Book Value %</span></nobr></DIV>
<DIV style="position:absolute;top:1040;left:198"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1040;left:239"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1040;left:281"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1040;left:319"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1055;left:75"><nobr><span class="ft273">Stock Total Return %</span></nobr></DIV>
<DIV style="position:absolute;top:1055;left:198"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1055;left:239"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1055;left:281"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1055;left:319"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:953;left:348"><nobr><span class="ft276">Quarterly Revenue &amp; EPS</span></nobr></DIV>
<DIV style="position:absolute;top:967;left:348"><nobr><span class="ft277">Revenue (Mil)</span></nobr></DIV>
<DIV style="position:absolute;top:967;left:425"><nobr><span class="ft12">Mar</span></nobr></DIV>
<DIV style="position:absolute;top:967;left:467"><nobr><span class="ft12">Jun</span></nobr></DIV>
<DIV style="position:absolute;top:967;left:507"><nobr><span class="ft12">Sep</span></nobr></DIV>
<DIV style="position:absolute;top:967;left:547"><nobr><span class="ft12">Dec</span></nobr></DIV>
<DIV style="position:absolute;top:967;left:583"><nobr><span class="ft12">Total</span></nobr></DIV>
<DIV style="position:absolute;top:981;left:348"><nobr><span class="ft12">2017</span></nobr></DIV>
<DIV style="position:absolute;top:981;left:430"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:981;left:470"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:981;left:511"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:981;left:551"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:981;left:581"><nobr><span class="ft12">817.3</span></nobr></DIV>
<DIV style="position:absolute;top:994;left:348"><nobr><span class="ft12">2016</span></nobr></DIV>
<DIV style="position:absolute;top:994;left:430"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:994;left:470"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:994;left:511"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:994;left:551"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:994;left:592"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1008;left:348"><nobr><span class="ft12">2015</span></nobr></DIV>
<DIV style="position:absolute;top:1008;left:430"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1008;left:470"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1008;left:511"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1008;left:551"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1008;left:592"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1021;left:348"><nobr><span class="ft12">2014</span></nobr></DIV>
<DIV style="position:absolute;top:1021;left:430"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1021;left:470"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1021;left:511"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1021;left:551"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1021;left:592"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1037;left:348"><nobr><span class="ft280">Earnings Per Share ()</span></nobr></DIV>
<DIV style="position:absolute;top:1050;left:348"><nobr><span class="ft12">2017</span></nobr></DIV>
<DIV style="position:absolute;top:1050;left:430"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1050;left:470"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1050;left:505"><nobr><span class="ft12">0.33</span></nobr></DIV>
<DIV style="position:absolute;top:1050;left:546"><nobr><span class="ft12">0.94</span></nobr></DIV>
<DIV style="position:absolute;top:1050;left:586"><nobr><span class="ft12">4.51</span></nobr></DIV>
<DIV style="position:absolute;top:1064;left:348"><nobr><span class="ft12">2016</span></nobr></DIV>
<DIV style="position:absolute;top:1064;left:430"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1064;left:470"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1064;left:511"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1064;left:551"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1064;left:586"><nobr><span class="ft12">3.17</span></nobr></DIV>
<DIV style="position:absolute;top:1077;left:348"><nobr><span class="ft12">2015</span></nobr></DIV>
<DIV style="position:absolute;top:1077;left:430"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1077;left:470"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1077;left:511"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1077;left:551"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1077;left:592"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1091;left:348"><nobr><span class="ft12">2014</span></nobr></DIV>
<DIV style="position:absolute;top:1091;left:430"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1091;left:470"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1091;left:511"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1091;left:551"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:1091;left:592"><nobr><span class="ft12">--</span></nobr></DIV>
<DIV style="position:absolute;top:953;left:621"><nobr><span class="ft285">Revenue Growth Year On Year %</span></nobr></DIV>
<DIV style="position:absolute;top:1084;left:621"><nobr><span class="ft8">2015</span></nobr></DIV>
<DIV style="position:absolute;top:1084;left:649"><nobr><span class="ft8">2016</span></nobr></DIV>
<DIV style="position:absolute;top:1084;left:762"><nobr><span class="ft8">2017</span></nobr></DIV>
<DIV style="position:absolute;top:19;left:75"><nobr><span class="ft304">Quantitative Equity Report | Release: 03 Sep 2018, 16:00 UTC | Reporting Currency: DKK | Trading Currency: DKK | Exchange:XCSE</span></nobr></DIV>
<DIV style="position:absolute;top:1141;left:75"><nobr><span class="ft337">© Morningstar 2018. All Rights Reserved. Unless otherwise provided in a separate agreement, you may use this report only in the country in which its original distributor is based. The information, data, analyses and</span></nobr></DIV>
<DIV style="position:absolute;top:1150;left:75"><nobr><span class="ft372">opinions presented herein do not constitute investment advice; are provided solely for informational purposes and therefore is not an offer to buy or sell a security; are not warranted to be correct, complete or accurate; and</span></nobr></DIV>
<DIV style="position:absolute;top:1159;left:75"><nobr><span class="ft404">are subject to change without notice. Except as otherwise required by law, Morningstar shall not be responsible for any trading decisions, damages or other losses resulting from, or related to, the information, data,</span></nobr></DIV>
<DIV style="position:absolute;top:1169;left:75"><nobr><span class="ft436">analyses or opinions or their use. The information herein may not be reproduced, in any manner without the prior written consent of Morningstar. Please see important disclosures at the end of this report.</span></nobr></DIV>
<DIV style="position:absolute;top:1146;left:778"><nobr><span class="ft16">ß</span></nobr></DIV>
<DIV style="position:absolute;top:1159;left:873"><nobr><span class="ft17">®</span></nobr></DIV>
<DIV style="position:absolute;top:17;left:833"><nobr><span class="ft439">Page 1 of 4</span></nobr></DIV>
</DIV>
</BODY>
</HTML>
"""

soup = BeautifulSoup (html, "html.parser")
# company_name = soup.find("span", attrs={"class": "ft22"}).text
# print("company_name : ",company_name)
last_close_price = soup.select(".ft6")[0]
last_close_price = last_close_price.get_text()
print("close price : ",last_close_price)
fair_value = soup.select(".ft6")[1]
fair_value = fair_value.get_text()
print("fair_value : ",fair_value)
discount = soup.select(".ft12")[16]
discount = float(discount.get_text())
print(soup.body.span.get_text())
print ("discount : ",discount)

