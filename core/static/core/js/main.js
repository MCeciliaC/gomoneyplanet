
function abrir_modal_edicion(url) {
    $('#edicion').load(url, function() {
        $(this).modal('show');
    });    
}

function abrir_modal_creacion(url) {
    $('#creacion').load(url, function() {
        $(this).modal('show');
    });    
}

function cerrar_modal_edicion() {
    $('#edicion').modal('hide');    
}

function cerrar_modal_creacion() {
    $('#creacion').modal('hide');    
}

function registrar() {
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function(response) {

        },
        error: function(error) {
            
        }
    });
}