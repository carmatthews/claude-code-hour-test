/* Webinar landing page client-side scripts */

(function () {
  "use strict";

  // --- Countdown Timer ---
  function updateCountdown() {
    fetch("/api/countdown")
      .then((r) => r.json())
      .then((data) => {
        document.getElementById("cd-days").textContent = data.days;
        document.getElementById("cd-hours").textContent = data.hours;
        document.getElementById("cd-minutes").textContent = data.minutes;
        document.getElementById("cd-seconds").textContent = data.seconds;

        if (data.passed) {
          document.getElementById("countdown").classList.add("countdown-passed");
        }
      })
      .catch(() => {});
  }

  setInterval(updateCountdown, 1000);

  // --- Registration Form ---
  var form = document.getElementById("registration-form");
  var message = document.getElementById("form-message");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      message.textContent = "";
      message.className = "form-message";

      var data = {
        first_name: document.getElementById("first_name").value,
        last_name: document.getElementById("last_name").value,
        email: document.getElementById("email").value,
        company: document.getElementById("company").value,
        role: document.getElementById("role").value,
      };

      fetch("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      })
        .then(function (r) {
          return r.json().then(function (body) {
            return { ok: r.ok, body: body };
          });
        })
        .then(function (result) {
          if (result.ok) {
            message.textContent = result.body.message;
            message.classList.add("success");
            form.reset();
          } else {
            message.textContent = result.body.errors.join(". ");
            message.classList.add("error");
          }
        })
        .catch(function () {
          message.textContent = "Something went wrong. Please try again.";
          message.classList.add("error");
        });
    });
  }

  // --- Smooth Scroll ---
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var target = document.querySelector(this.getAttribute("href"));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  // --- Interactive Terminal ---
  var terminalTyped = document.getElementById("terminal-typed");
  var terminalCursor = document.getElementById("terminal-cursor");
  var terminalOutput = document.getElementById("terminal-output");
  var clawdContainer = document.getElementById("clawd-container");
  var terminalBuffer = "";

  if (terminalCursor) {
    setInterval(function () {
      terminalCursor.style.opacity = terminalCursor.style.opacity === "0" ? "1" : "0";
    }, 530);
  }

  if (terminalTyped) {
    document.addEventListener("keydown", function (e) {
      // Ignore if user is focused on a form input
      var tag = document.activeElement.tagName;
      if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;

      if (e.key === "Backspace") {
        e.preventDefault();
        terminalBuffer = terminalBuffer.slice(0, -1);
        terminalTyped.textContent = terminalBuffer;
        terminalOutput.textContent = "";
        clawdContainer.innerHTML = "";
      } else if (e.key === "Enter") {
        e.preventDefault();
        handleTerminalCommand(terminalBuffer.trim().toLowerCase());
        terminalBuffer = "";
        terminalTyped.textContent = "";
      } else if (e.key.length === 1 && !e.ctrlKey && !e.metaKey) {
        e.preventDefault();
        terminalBuffer += e.key;
        terminalTyped.textContent = terminalBuffer;
        terminalOutput.textContent = "";
        clawdContainer.innerHTML = "";
      }
    });
  }

  function handleTerminalCommand(cmd) {
    if (cmd === "clawd") {
      terminalOutput.textContent = "";
      showClawd();
    } else if (cmd === "/help") {
      terminalOutput.textContent =
        "Available commands:\n" +
        "  /help     Show this message\n" +
        "  clawd     ???";
    } else if (cmd === "") {
      terminalOutput.textContent = "";
    } else {
      terminalOutput.textContent = 'Try typing "clawd" or "/help"';
    }
  }

  function showClawd() {
    clawdContainer.innerHTML = "";
    var wrapper = document.createElement("div");
    wrapper.style.display = "flex";
    wrapper.style.flexDirection = "column";
    wrapper.style.alignItems = "center";

    var sprite = document.createElement("div");
    sprite.className = "clawd-sprite";
    var c = "#d97757";
    sprite.style.boxShadow = [
      /* head */
      "2px 0 0 "+c, "3px 0 0 "+c, "4px 0 0 "+c, "5px 0 0 "+c,
      "6px 0 0 "+c, "7px 0 0 "+c, "8px 0 0 "+c, "9px 0 0 "+c, "10px 0 0 "+c,
      "2px 1px 0 "+c, "3px 1px 0 "+c, "4px 1px 0 "+c, "5px 1px 0 "+c,
      "6px 1px 0 "+c, "7px 1px 0 "+c, "8px 1px 0 "+c, "9px 1px 0 "+c, "10px 1px 0 "+c,
      /* eyes row */
      "2px 2px 0 "+c, "3px 2px 0 #222", "4px 2px 0 "+c, "5px 2px 0 "+c,
      "6px 2px 0 "+c, "7px 2px 0 "+c, "8px 2px 0 "+c, "9px 2px 0 #222", "10px 2px 0 "+c,
      /* lower head */
      "2px 3px 0 "+c, "3px 3px 0 "+c, "4px 3px 0 "+c, "5px 3px 0 "+c,
      "6px 3px 0 "+c, "7px 3px 0 "+c, "8px 3px 0 "+c, "9px 3px 0 "+c, "10px 3px 0 "+c,
      /* body with side nubs */
      "1px 4px 0 "+c, "2px 4px 0 "+c, "3px 4px 0 "+c, "4px 4px 0 "+c, "5px 4px 0 "+c,
      "6px 4px 0 "+c, "7px 4px 0 "+c, "8px 4px 0 "+c, "9px 4px 0 "+c,
      "10px 4px 0 "+c, "11px 4px 0 "+c,
      /* lower body */
      "2px 5px 0 "+c, "3px 5px 0 "+c, "4px 5px 0 "+c, "5px 5px 0 "+c,
      "6px 5px 0 "+c, "7px 5px 0 "+c, "8px 5px 0 "+c, "9px 5px 0 "+c, "10px 5px 0 "+c,
      /* legs — 4 legs, two grouped left + two grouped right, outer aligned with body */
      "2px 6px 0 "+c, "4px 6px 0 "+c, "8px 6px 0 "+c, "10px 6px 0 "+c,
      "2px 7px 0 "+c, "4px 7px 0 "+c, "8px 7px 0 "+c, "10px 7px 0 "+c
    ].join(",");

    var label = document.createElement("div");
    label.className = "clawd-label";
    label.textContent = "clawd says hi!";

    wrapper.appendChild(sprite);
    wrapper.appendChild(label);
    clawdContainer.appendChild(wrapper);
  }
})();
