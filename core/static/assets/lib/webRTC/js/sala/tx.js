
var connection = new RTCMultiConnection();
connection.socketURL = 'http://localhost:9001/';

initOneToMany();


function initOneToMany(){

    connection.socketMessageEvent = 'audio-conference-demo';

    connection.session = {
        audio: true,
        video: false,
        broadcast: true
    };

    connection.mediaConstraints = {
        audio: true,
        video: false,
    };

    connection.sdpConstraints.mandatory = {
        OfferToReceiveAudio: true,
        OfferToReceiveVideo: false
    };

    connection.preferSCTP = false;


    connection.audiosContainer = $('#audios-container-ul')[0];
    connection.onstream = function(event) {
        var width = parseInt(connection.audiosContainer.clientWidth / 2) - 20;
        var mediaElement = getHTMLMediaElement(event.mediaElement, {
            title: event.userid,
        });

        connection.audiosContainer.appendChild(mediaElement);

        setTimeout(function() {
            mediaElement.media.play();
        }, 5000);

        mediaElement.id = event.streamid;

    };
}

onnection.openOrJoin(romId);
