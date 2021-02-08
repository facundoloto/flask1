const btnDelete= document.querySelectorAll('.btn-delete');
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      Swal.fire({
        title: 'Desea elimnar este usuario?',
        text: "Una vez borrado no se podra recuperar el usuario!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Aceptar'
      }).then((result) => {
        if (!result.isConfirmed) {
          Swal.fire(
            e.preventDefault(),
            'Eliminado!',
            'El usuario se elimino.',
            'success'
          )
         
        }
      })
    
    });
  })
}
