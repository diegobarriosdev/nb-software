//Numbot responses
	function rnActivityOneMomentOne(ur,nbcom){	
		if(havenumbers(ur)!=0){
			switch(nbcom){
				case 1:
					if(/1/.test(ur)&&ur.length==1){
						playSequenceOne("s",'d28');}						  
					else{ 
						playSequenceOne("e",'d28');}						
					break;				
				case 2:
					if(/2/.test(ur)&&ur.length==1){
						playSequenceOne("s",'d29');}						  
					else{ 
						playSequenceOne("e",'d29');}
					break;
				
				case 3:
					if(/3/.test(ur)&&ur.length==1){
						playSequenceOne("s",'d30');}						  
					else{ 
						playSequenceOne("e",'d30');}
					break;
				
				case 4:
				if(/4/.test(ur)&&ur.length==1){
						playSequenceOne("s",'d31');}						  
					else{ 
						playSequenceOne("e",'d31');}
					break;
				
				case 5:
					if(/5/.test(ur)&&ur.length==1){
						playSequenceOne("s",'d32');}						  
					else{ 
						playSequenceOne("e",'d32');}
					break;
				
				case 6:
					if(/6/.test(ur)&&ur.length==1){
						playSequenceOne("s",'d33');}						  
					else{ 
						playSequenceOne("e",'d33');}
					break;
								
				case 7:
					if(/7/.test(ur)&&ur.length==1){
						playSequenceOne("s",'d34');}						  
					else{ 
						playSequenceOne("e",'d34');}
					break;
										
				case 8:
					if(/8/.test(ur)&&ur.length==1){
						playSequenceOne("s",'d35');}						  
					else{ 
						playSequenceOne("e",'d35');}
					break;			
				
				case 9:
					if(/9/.test(ur)&&ur.length==1){
						playSequenceOne("s",'d36');}						  
					else{ 
						playSequenceOne("e",'d36');}
					break;

				default:
					alert("Error");
					playSound('d96');
			}
		}else{
			playSound('d94');
		}
	}

	function rnActivityTwoMomentOne(ur,nbc,co){
		if(havenumbers(ur)!=0){
			switch(nbc){
				case 1:
					if(/1/.test(ur)&&ur.length==1){ 
						waitAndPlay(0,'d22');
					}else { rnMssgError2(nbc,co); } 
					break;				
				case 2:
					if((/2/.test(ur)&&ur.length==1) || ur=="DOS" || ur=="dos" || ur=="Dos"){
					 	waitAndPlay(0,'d22');
					 }else { rnMssgError2(nbc,co); }
					 break;
				case 3:
					if(/3/.test(ur)&&ur.length==1){
					 	waitAndPlay(0,'d22');
					}else { rnMssgError2(nbc,co); } 
					break;
				default:
					rnMssgError2(nbc,co);
					break;
			}
			setTimeout(function(){
				show('#div-a2-rv-1-s');
			},time(3));			
		}else{
			waitAndPlay(time(0),'d94');
			setTimeout(function(){
				show('#div-a2-rv-1-e');
			},time(3));
		}
		hide('#rec');
	}

	function playSequenceOne(e,number){
		hide('#rec');		
		if(e=="s"){
			setTimeout(function(){ playSound('d90'); }, 0);
			setTimeout(function(){ playSound('d06'); }, time(0.5));
			setTimeout(function(){ playSound(number); },time(3));
			setTimeout(function(){ playSound('d42'); }, time(4));
			setTimeout(function(){ playSound('d08'); }, time(5));
			setTimeout(function(){ 
				show('#div-a1-rv-1-s');
			},time(8));
		}else if(e=="e"){
			setTimeout(function(){ playSound('d91'); }, 0);
			setTimeout(function(){ playSound('d07'); }, time(0.5));
			setTimeout(function(){ playSound(number); },time(3));
			setTimeout(function(){ playSound('d42'); }, time(4));
			setTimeout(function(){ 
				show('#div-a1-rv-1-e');
			},time(8));
		}		
	}

	function blockColor(color){
		waitAndPlay(0,'d87');
		switch(color){
			case 'r': a='d38'; break;
			case 'g': a='d41'; break;
			case 'b': a='d40'; break;}
		waitAndPlay(time(1.5),a);
		waitAndPlay(time(2.5),'d88');
	}

	function rnMssgSuccess2(nb,color){
		waitAndPlay(time(0),'d15');
	}

	function rnMssgError2(nb,co){
		waitAndPlay(0,'d07');
		setTimeout(function(){
			rnBlockAndColor(nb,co);
		},time(3));
	}

	function rnBlockAndColor(nb,co){
		if(!isNaN(nb)&&nb!=0){
			waitAndPlay(time(0),numberSound(nb));
			waitAndPlay(time(1),'d42');
			waitAndPlay(time(2),co);
		}
	}

	function numbotResponse(ur){
		if(exist('#div-a1-rv-1')){
			var n=parseInt($('#nbCOM').text());
			rnActivityOneMomentOne(ur,n);
		}else if(exist('#div-stg-02-02')){
			nrc=parseInt($('#rc').text());
			//Hasya aqui bien
			rnActivityTwoMomentOne(ur,nrc,'d38');
		}else if(exist('#div-stg-02-03')){
			nbgc=parseInt($('#gc').text());
			rnActivityTwoMomentOne(ur,nbgc,'d41');
		}else if(exist('#div-stg-02-04')){
			nbbc=parseInt($('#bc').text());
			rnActivityTwoMomentOne(ur,nbbc,'d40');
		}
	}

	

	
