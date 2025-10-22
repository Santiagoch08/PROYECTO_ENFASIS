document.addEventListener("DOMContentLoaded", function () {
  // Eliminar
  var confirmDeleteModal = document.getElementById("confirmDeleteModal");
  confirmDeleteModal.addEventListener("show.bs.modal", function (event) {
    var button = event.relatedTarget;
    var userId = button.getAttribute("data-userid");
    var form = confirmDeleteModal.querySelector("#deleteForm");
    form.action = "/delete/" + userId;
  });

  // Editar
  var editUserModal = document.getElementById("editUserModal");
  editUserModal.addEventListener("show.bs.modal", function (event) {
    var button = event.relatedTarget;
    var id = button.getAttribute("data-id");
    var name = button.getAttribute("data-name");
    var email = button.getAttribute("data-email");
    var rol = button.getAttribute("data-rol");
    var enfasis = button.getAttribute("data-enfasis");

    document.getElementById("editName").value = name;
    document.getElementById("editEmail").value = email;
    document.getElementById("editRol").value = rol;
    document.getElementById("editEnfasis").value = enfasis;

    var form = document.getElementById("editUserForm");
    form.action = "/edit/" + id;
  });
});
