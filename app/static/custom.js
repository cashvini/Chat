let menu = document.querySelector('#menu-icon');
let navlist =  document.querySelector('.navlist');
menu.onclick = () => {
  menu.classList.toggle('bx-x');
  navlist.classList.toggle('open');

  console.log(navlist);
};
$(function () {
  let INDEX = 0;
  $("#chat-submit").click(function (e) {
    e.preventDefault();
    const msg = $("#chat-input").val();
    if (msg.trim() === "") {
      return false;
    }
    const el = document.getElementsByClassName("chat-box-body");
    // id of the chat container ---------- ^^^
    
    generate_message(msg, "self");
    submit_message(msg);
  });

  function submit_message(message) {
    const sendRequest = $.post("/chat", { message: message });
    sendRequest.done(function (data) {
      console.log(data);
      generate_message(data.message, "user");
      if (data && data.payload !== null) {
        const buttons = data.payload.suggestion_chips;
        let srtButton = "";
        buttons.map(
          (button) =>
            (srtButton +=
              '<button type="button" class="btn btn-outline-secondary mr-1 btn-chips" onclick="$(\'#chat-input\').val(\'' +
              button +
              "');$('#chat-submit').click();\">" +
              button +
              "</button>")
        );
        generate_message(srtButton, "button");
      }
    });
  }

  function generate_message(msg, type) {
    $("#messageFormeight").animate({ scrollTop: 2000000 }, "slow");
    const chatLogs = $(".chat-logs");
    INDEX++;
    let str = "";

    str += "<div id='cm-msg-" + INDEX + "' class=\"chat-msg " + type + '">';
    const date = new Date();
    const hour = date.getHours();
    const minute = date.getMinutes();
    const str_time = hour + ":" + minute;
    if (type == "self") {
      var userHtml =
        '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">' +
        msg +
        '<span class="msg_time_send"  style="color:white">' +
        str_time +
        '</span></div><div class="img_cont_msg"><img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="rounded-circle user_img_msg"></div></div>';
      $("#messageFormeight").append(userHtml);
    } else if (type == "user") {
      var botHtml =
        '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">' +
        msg +
        '<span class="msg_time" style="color:white">' +
        str_time +
        "</span></div></div>";
      $("#messageFormeight").append($.parseHTML(botHtml));
      $("#chat-input").val("");
    } else {
      str += '<div class="cm-msg-buttons">';
      str += msg;
      str += "</div>";
    }
    if (type === "self") {
      $("#chat-input").val("");
    }
    str += "</div>";
    chatLogs.append(str);
    $("#cm-msg-" + INDEX)
      .hide()
      .fadeIn(300);
    chatLogs.stop().animate({ scrollTop: chatLogs[0].scrollHeight }, 1000);
  }

  $(document).delegate(".chat-btn", "click", function () {
    const value = $(this).attr("chat-value");
    const name = $(this).html();
    $("#chat-input").attr("disabled", false);
    generate_message(name, "self");
  });

  $("#chat-circle").click(function () {
    $("#chat-circle").toggle("scale");
    $(".chat-box").toggle("scale");
  });

  $(".chat-box-toggle").click(function () {
    $("#chat-circle").toggle("scale");
    $(".chat-box").toggle("scale");
  });
});
