//Global Variables
//To HTML elements
	function show(element){
		$(element).show();
	}

	function hide(element){
		$(element).hide();
	}

//To Object Audio
	function playSound(audio){
		var audio = new Audio('static/aud/'+audio+'.wav');
		audio.play();
	}

	function waitAndPlay(pause,sound){
		setTimeout(function(){ playSound(sound); },pause);
	}

//To Pauses  and Times
	function time(seconds){
		return (1000*seconds);
	}

	function pause(millis)
	{
		var date = new Date();
		var curDate = null;
		do { curDate = new Date(); }
		while(curDate-date < millis);
	}

//Validations
	function exist(element){
		return $(element).length;
	}

	function havenumbers(text){
	  	var numb="0123456789";
	   	for(i=0; i<text.length; i++){
		  	if (numb.indexOf(text.charAt(i),0)!=-1){
			 	return 1;
		 	 }
	   	}
	   return 0;	
	}

//Select Audios
	function numberSound(xnumber){
		nnumber='';
		switch(xnumber){
			case 1: nnumber='d28';	break;
			case 2: nnumber='d29';	break;
			case 3: nnumber='d30';	break;
			case 4: nnumber='d31';	break;
			case 5: nnumber='d32';	break;
			case 6: nnumber='d33';	break;
			case 7: nnumber='d34';	break;
			case 8: nnumber='d35';	break;
			case 9: nnumber='d36';	break;
			default:
				nnumber='d97';
		}
		return nnumber;
	}

//Test
function hola(){
	return 'Estoy accediendo a functions.js';	
}

