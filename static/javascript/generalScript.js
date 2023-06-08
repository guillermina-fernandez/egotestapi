function edit_product(pk){
    var row = document.getElementById(pk);
    var tds = row.getElementsByTagName('td');
    product_id.value = pk;
    id_product_name.value = tds[1].textContent;
    id_model.value = tds[2].textContent;
    for (var i = 0; i < id_type.options.length; i++) {
        if (id_type.options[i].text === tds[3].textContent) {
            id_type.options[i].selected = true;
            break;
        };
    };
    id_year.value = tds[4].textContent;
    id_price.value = tds[5].textContent;
    btn_save.name = "btn_save_changes";
    btn_delete.removeAttribute('hidden');
};


function confirm_submit(){
    const clickedButton = event.submitter;
    if (clickedButton.name === 'btn_delete'){
        let accepted = confirm('ATENCIÓN!\n¿Desea eliminar el registro definitivamente?')
        if (!accepted){
            event.preventDefault();
        };
    };
};


function search_item(table_id) {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("input_search");
    filter = input.value.toUpperCase();
    table = document.getElementById(table_id);
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                };
            };
    };
};


function ChangeRowColor(tableRow, highlight){
    if (highlight){
        tableRow.style.backgroundColor = '#dcfac9';
    } else {
        tableRow.style.backgroundColor = 'white';
    };
};