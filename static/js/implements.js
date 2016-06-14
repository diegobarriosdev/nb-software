//Global Variables
var swr=0;
var swg=0;
var swb=0;

//Implements
	if(exist('#div-welcome')){
		waitAndPlay(0,'d01');
		waitAndPlay(time(5),'d02');
		setTimeout(function(){
			show('#div-welcome');
			},time(10));
				
	}

	if(exist('#div-a1-01')){
		var n=parseInt($('#nbCOM').text());
		waitAndPlay(0,'d03');
		waitAndPlay(time(4),'d04');
		setTimeout(function(){
			show('#div-a1-01');
			},time(n*7));
	}

	if(exist('#div-a1-rv-1')){
		var n=parseInt($('#nbCOM').text());
		waitAndPlay(0,'d05');
		enableRecognition();
	}

	if(exist('#div-a1-rc1')){
		var nbCom=parseInt($('#nbCOM').text());
		var nbPlayer=parseInt($('#nbPlayer').text());
		if(nbPlayer!=0){
			if(nbPlayer!=nbCom){
				waitAndPlay(time(0.5),'d10');
				waitAndPlay(time(3),numberSound(nbCom));
				waitAndPlay(time(4),'d42');
				waitAndPlay(time(5),'d11');
				setTimeout(function(){
					show('#div-a1-rc1-e');
				},time(8));
			}else{
				waitAndPlay(time(0.5),'d09');
				waitAndPlay(time(3),numberSound(nbPlayer));
				waitAndPlay(time(3.5),'d42');
				waitAndPlay(time(5),'d12');
				waitAndPlay(time(7),'d13');
				setTimeout(function(){
					show('#div-a1-rc1-s');
				},time(8));
			}
		}else{
			waitAndPlay(time(0.5),'d93');
			waitAndPlay(time(3.5),'d97');
			setTimeout(function(){
					show('#div-a1-rc1-e');
				},time(7.5));
		}
	}

	if(exist('#div-stg-a1-02')){
		waitAndPlay(0,'d14');
		setTimeout(function(){ 
			show('#div-stg-a1-02')},time(10));
	}

	if(exist('#div-a1-rc2')){
		var n=parseInt($('#nbPlayer').text());
		if(n!=0){
			waitAndPlay(time(0.5),'d15');
			waitAndPlay(time(3),numberSound(n));
			waitAndPlay(time(3.5),'d42');
			waitAndPlay(time(5),'d16');
			setTimeout(function(){
				waitAndPlay(0,'d90');
				waitAndPlay(time(0.5),'d17');
				waitAndPlay(time(2.5),numberSound(n));
				waitAndPlay(time(3.5),'d42');
				waitAndPlay(time(4),'d18');
				show('#div-a1-rc2-s');
				},time(n*7));
		}else{
			waitAndPlay(0,'d97');
		}
	}


	if(exist('#div-stg-02-01')){
		waitAndPlay(time(0),'d04');
		var t=parseInt($('#tbCom').text());
		setTimeout(function(){
			show('#div-a2-01-1');
			waitAndPlay(time(0),'d90');
		},time(t*8));
	}

	if(exist('#div-stg-02-02')){
		blockColor('r');	
		enableRecognition();
	}

	if(exist('#div-stg-02-03')){
		blockColor('g');	
		enableRecognition();
	}

	if(exist('#div-stg-02-04')){		
		blockColor('b');	
		enableRecognition();
	}

	if(exist('#div-stg-02-05')){
		waitAndPlay(time(1),'d20');
		setTimeout(function(){
			show('#div-a2-rc-1');
		},time(5));
	}

	if(exist('#div-stg-02-06')){
		var rc=parseInt($('#rc').text());
		var gc=parseInt($('#gc').text());
		var bc=parseInt($('#bc').text());
		var rp=parseInt($('#rp').text());
		var gp=parseInt($('#gp').text());
		var bp=parseInt($('#bp').text());
		if(rc==rp&&gc==gp&&bc==bp){	
			if(rp!=0){setTimeout(function(){
				rnBlockAndColor(rp,'d38');
			},time(3));}

			if(gp!=0){setTimeout(function(){
				rnBlockAndColor(gp,'d41');
			},time(7));}

			if(bp!=0){setTimeout(function(){
				rnBlockAndColor(bp,'d40');
			},time(10));}	

			rnMssgSuccess2(rp,'d38');
			rnMssgSuccess2(gp,'d42');
			rnMssgSuccess2(bp,'d41');
		}else{
			waitAndPlay(0,'d10');
			if(rc!=0){setTimeout(function(){
				rnBlockAndColor(rc,'d38');
			},time(4));}

			if(gc!=0){setTimeout(function(){
				rnBlockAndColor(gc,'d41');
			},time(7));}
				
			if(bc!=0){setTimeout(function(){
				rnBlockAndColor(bc,'d40');
			},time(10));}						
		}
		waitAndPlay(time(15),'d27');
		waitAndPlay(time(18),'d13');
	}








