

function beforeJoiningARoom(callback) {
    connection.extra.broadcaster = false;
    connection.dontCaptureUserMedia = true;
    connection.session.oneway = true;
    callback();
}

var connection = new RTCMultiConnection();

connection.socketURL = 'http://localhost:9001/';
connection.socketMessageEvent = 'audio-conference-demo';
connection.userid = firstName + " " + lastName;


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


var countConnect = 0;
connection.audiosContainer = document.getElementById('audios-container');
connection.onstream = function(event) {
    var width = parseInt(connection.audiosContainer.clientWidth / 2) - 20;
    var mediaElement = getHTMLMediaElement(event.mediaElement, {
        title: event.userid,
    });

    connection.audiosContainer.appendChild(mediaElement);
    countConnect += 1;
    if(countConnect >  0){
        $("#id_RX_h1").text(username + " <- " + romName);
    }

    setTimeout(function() {
        mediaElement.media.play();
    }, 5000);

    mediaElement.id = event.streamid;

    connection.preferSCTP = false;

};

connection.onstreamended = function(event) {
    var mediaElement = document.getElementById(event.streamid);
    if (mediaElement) {
        mediaElement.parentNode.removeChild(mediaElement);
        countConnect -= 1;
        if(countConnect < 1){
          location.reload();
       }
    }
};

function joinBroadcastLooper(roomid) {

    (function reCheckRoomPresence() {
        connection.checkPresence(roomid, function(isRoomExist) {
            if (isRoomExist) {
                beforeJoiningARoom(function() {
                    connection.join(roomid, function() {
                    });
                });
                return;
            }
            setTimeout(reCheckRoomPresence, 5);
        });
    })();
}

joinBroadcastLooper(romId);
