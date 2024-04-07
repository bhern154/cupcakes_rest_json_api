// GET API request to get all cupcakes
async function getAllCupcakes() {
    const response = await axios.get('/api/cupcakes');
    return response.data;
}

// Try catch handling for GET request
(async () => {
    try {
        const cupcakes = await getAllCupcakes();
        await listCupcakes(cupcakes);
    } catch (error) {
        console.error('Error fetching cupcakes:', error);
    }
})();

// list cupcakes by appending code to the .container div
async function listCupcakes(cupcakes) {

    const $mainContent = $('.container');

    cupcakes.cupcakes.forEach(cupcake => {
        htmlContent = cupcake_to_html(cupcake.id, cupcake.image, cupcake.flavor, cupcake.size, cupcake.rating)
        $mainContent.prepend(htmlContent);
      });
}

// handle cupcake form (POST requst and append to .container div)
$('.cupcake_form').submit(function(event) {

    event.preventDefault();

    // Extract data from the form
    const $mainContent = $('.container');
    var cupcakeForm = {
        "flavor": $('input[name="flavor"]').val(),
        "size": $('input[name="size"]').val(),
        "rating": $('input[name="rating"]').val(),
        "image": $('input[name="image"]').val()
    };

    // POST request using axios
    axios.post('/api/cupcakes', cupcakeForm)
            .then(function(response) {
                resp = response.data                
                htmlContent = cupcake_to_html(resp.cupcake.id, resp.cupcake.image, resp.cupcake.flavor, resp.cupcake.size, resp.cupcake.rating)
                $mainContent.prepend(htmlContent);
            })
            .catch(function(error) {
                console.error(error);
            });

});

// function to create html content with the cupcake info
function cupcake_to_html(id, image, flavor, size, rating){
    trashIconURL = 'https://cdn-icons-png.freepik.com/512/6861/6861362.png'
    const htmlContent = `
        <div class="boxed-content">
            <button class="trash" data-id="${id}"><img class="trashImg" src="${trashIconURL}" height='50'></button>
            <img src="${image}" height='100'>
            <p>Flavor: <strong>${flavor}</strong></p>
            <p>Size: <strong>${size}</strong></p>
            <p>Rating: <strong>${rating}/5</strong></p>
        </div>
    `;
    return htmlContent;
}

// DELETE request using axios
$(document).ready(function() {
    $(document).on('click', '.trash', deleteCupcake);
});

async function deleteCupcake(){
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()
}