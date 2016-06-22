//Voice recognition
var accessToken = "9d2f8c9237de40a69bb7d324891fc0ee";
var baseUrl = "https://api.api.ai/v1/";
var recognition;
var userResponse;

	function enableRecognition(){
		$(document).ready(function() {
			$("#input").keypress(function(event) {
				if (event.which == 5) {
					event.preventDefault();
					send();
				}
			});
			$("#rec").click(function(event) {
				switchRecognition();
			});
		});
	}

	function startRecognition() {
	recognition = new webkitSpeechRecognition();
		recognition.onstart = function(event) {
			updateRec();
		};
		recognition.onresult = function(event) {
			var text = "";
			for (var i = event.resultIndex; i < event.results.length; ++i) {
				text += event.results[i][0].transcript;
			}
			setInput(text);
			stopRecognition();
		};
		recognition.onend = function() {
			stopRecognition();
		};
		recognition.lang = "es-ES";
		recognition.start();
	}
		
	function stopRecognition() {
		if (recognition) {
			recognition.stop();
			recognition = null;
		}
		updateRec();
	}

	function switchRecognition() {
		if (recognition) {
			stopRecognition();
		} else {
			startRecognition();
		}
	}

	function updateRec() {
		//$("#rec").text(recognition ? "Detener" : "Hablar");
		if(recognition){
			$("#irec").remove();
			$("#rec").append( "<i id='stop' class='fa fa-stop-circle-o fa-5x' aria-hidden='true'></i>" );
		}else{
			$("#irec").remove();
			$('#stop').remove();
			$('#rec').append("<i id='irec' class='fa fa-microphone fa-5x' aria-hidden='true'></i>");
		}
	}

	function send() {
		var text = $("#input").val();
		$.ajax({
			type: "POST",
			url: baseUrl + "query/",
			contentType: "application/json; charset=utf-8",
			dataType: "json",
			headers: {
				"Authorization": "Bearer " + accessToken
			},
			data: JSON.stringify({ q: text, lang: "en" }),

			success: function(data) {
				setResponse(JSON.stringify(data, undefined, 2));
			},
			error: function() {
				setResponse("Internal Server Error");
			}
		});
		setResponse("Loading...");
	}

	function setResponse(val) {
		$("#response").text(val);
	}

	function setInput(text) {
		$("#input").val(text);
		//send();
		userResponse=$("#input").val();
		//userResponse=5;
		numbotResponse(userResponse);		
	}