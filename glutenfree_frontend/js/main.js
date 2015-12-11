var template1 = Handlebars.templates['recipe_list'];

var template2 = Handlebars.templates['nav_list'];

var template3 = Handlebars.templates['pagination'];

var template4 = Handlebars.templates['recipe_detail'];

var page_letter = 'a'

var loadMain = function() { 

    $.ajax({
        type:'GET',
        url:'http://127.0.0.1:8000/recipe_list/'+page_letter,
        data:{},
        success: function(data) {
            list_template = template1(data);
            console.log(data)
            recipeList.html(list_template);

            pagination_template = template3(data);
            pagination.html(pagination_template);

            nav_template = template2(data);
            navList.html(nav_template);

        }
    })
};

var paginate = function() {
        $('#pagination').on('click', '.page-button', function(e) {

        console.log(e.target.id);

        $.ajax({
            type:'GET',
            url:'http://127.0.0.1:8000/recipe_list/'+page_letter,
            data:{'page': e.target.id, 'letter': page_letter},
            success: function(data) {

                list_template = template1(data)
                recipeList.html(list_template);

                pagination_template = template3(data);
                pagination.html(pagination_template);

            }
        })
    });
};

var listNav = function() {
    $('#nav-list').on('click', '.letter', function(e) {

        console.log(e.target.id);

        page_letter = e.target.id

        $.ajax({
        type:'GET',
        url:'http://127.0.0.1:8000/recipe_list/'+page_letter,
        data:{'letter': page_letter},
        success: function(data) {

            list_template = template1(data)
            recipeList.html(list_template);

            nav_template = template2(data);
            navList.html(nav_template);

            pagination_template = template3(data);
            pagination.html(pagination_template);

            }
        });

    });
};

var recipeDetail = function() {
        $('#recipe-list').on('click', '.recipe', function(e) {
        console.log(e.target.offsetParent.id)    
        $.ajax({
            type:'GET',
            url:'http://127.0.0.1:8000/recipe_detail/' + e.target.offsetParent.id,
            data:{},
            success: function(data) {
                html_template = template4(data);
                recipeList.html(html_template);

            }
        })
    });
};
$('.letters').on('click', function(e){
    console.log(e.target.id)
    page_letter = e.target.id
    loadMain()
})
