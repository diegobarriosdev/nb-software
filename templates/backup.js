		
			$( "#nb-c-COM" ).ready(function() {
				alert("hola");
				
					activeActivity=2;
					var ecolor="none";
					var nbrCOM=parseInt($('#nb-r-COM').text());
					var nbgCOM=parseInt($('#nb-g-COM').text());
					var nbbCOM=parseInt($('#nb-b-COM').text());
					time=(nbrCOM+nbgCOM+nbbCOM)*(1000);
					swr=0; swg=0; swb=0;
					alert("Estoy aqui...");
					pause(time);
					alert("Llegue aquí...");
					if(swr==0){
						playAskNumberColor("r");
					}

					showelement('btn-a2-rv-01',1000);				
					if(swr==0){
						alert("R voz:"+rv2);
						alert("Reds :"+nbrCOM);
						swr=playResponse(nbrCOM,rv2);
					}
										
				});


			$( "#btn03next" ).ready(function(){
				showelement("btn03next",8000);
			});			

			$( "#a1m2nbplayer" ).ready(function(){
				var n=parseInt($("#a1m2nbplayer").text());		
				if(!isNaN(n)){
					if(n>0&&n<=9){
						playsoundwithpause("d09",500);
						playsoundwithpause(choosingnumbersound(n),2500);
						playsoundwithpause("d42",3500);	
						playsoundwithpause("d16",6000);
						playsoundwithpause("d17",(n*50000));
						playsoundwithpause(choosingnumbersound(n),((n*50000)+1500));
						playsoundwithpause("d42",((n*50000)+2500));
						playsoundwithpause("d18",((n*50000)+8000));
						showelement("btn04camsucc",((n*50000)+8000));
					}else{
						playsoundwithpause("d97",500);
						playsoundwithpause("d95",3000);	
						showelement("btn05camerror",6000);
					}
				}
			});	

			function playResponse(nblock,nvoz){
				if(nblock!=nvoz){
					playsoundwithpause('d23',0);
					return 0;
				}else{
					playsoundwithpause('d22',0);
					return 1;
				}
			}

			function playAskNumberColor(ecolor){
				if(ecolor=="r"){
					choosseNumberColor("r");
				else if(ecolor=="g"){
					choosseNumberColor("g");
				}else if(ecolor=="b"){
					choosseNumberColor("b");
				}
			}

			function choosseNumberColor(swr){
				if(swr!=""){
					playsoundwithpause('d87',0);
					switch(swr){
						case "r":
							playsoundwithpause('d38',2500);
						case "g":
							playsoundwithpause('d41',2500);
						case "b":
							playsoundwithpause('d40',2500);
					}
					playsoundwithpause('d88',3500);				
				}else{
					playsoundwithpause('d96',1000);
				}				
			}

			
					
			