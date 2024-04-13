document.getElementById('id_commune').addEventListener('change', function() {
    var communeId = this.value;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_related_data/?commune_id=' + communeId, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);
            // Mettre à jour l'interface utilisateur avec les données récupérées
            console.log(data); // À remplacer par la mise à jour de l'interface utilisateur
        }
    };
    xhr.send();
});