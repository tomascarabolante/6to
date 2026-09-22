document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".brand-mark").forEach((mark) => {
    const logo = document.createElement("img");
    logo.className = "brand-logo";
    logo.src = "logo.svg";
    logo.alt = "";
    mark.replaceWith(logo);
  });

  const backToTop = document.querySelector("#backToTop");

  if (backToTop) {
    window.addEventListener("scroll", () => {
      backToTop.classList.toggle("visible", window.scrollY > 450);
    });

    backToTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  const contactForm = document.querySelector("#contactForm");
  const confirmation = document.querySelector("#formConfirmation");

  if (contactForm && confirmation) {
    contactForm.addEventListener("submit", (event) => {
      event.preventDefault();
      contactForm.classList.add("was-validated");

      if (!contactForm.checkValidity()) {
        confirmation.classList.add("d-none");
        return;
      }

      const name = document.querySelector("#nombre").value.trim();
      confirmation.textContent = `Gracias, ${name}. Recibimos tu mensaje y te responderemos dentro de 48 horas.`;
      confirmation.classList.remove("d-none");
      contactForm.reset();
      contactForm.classList.remove("was-validated");
    });
  }
});
