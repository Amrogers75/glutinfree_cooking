(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['recipe_detail'] = template({"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var helper, alias1=depth0 != null ? depth0 : {}, alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "<div class=\"row\" id=\""
    + alias4(((helper = (helper = helpers.pk || (depth0 != null ? depth0.pk : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"pk","hash":{},"data":data}) : helper)))
    + "\">\n  <div class=\"col-md-12\" id=\""
    + alias4(((helper = (helper = helpers.pk || (depth0 != null ? depth0.pk : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"pk","hash":{},"data":data}) : helper)))
    + "\">\n    <h2 class=\"recipe\" id=\""
    + alias4(((helper = (helper = helpers.pk || (depth0 != null ? depth0.pk : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"pk","hash":{},"data":data}) : helper)))
    + "\" >"
    + alias4(((helper = (helper = helpers.title || (depth0 != null ? depth0.title : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"title","hash":{},"data":data}) : helper)))
    + "</h2>\n       <ul>\n          <li>Glutenfree: "
    + alias4(((helper = (helper = helpers.glutenfree || (depth0 != null ? depth0.glutenfree : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"glutenfree","hash":{},"data":data}) : helper)))
    + "</li>\n          <li>Social_rank: "
    + alias4(((helper = (helper = helpers.social_rank || (depth0 != null ? depth0.social_rank : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"social_rank","hash":{},"data":data}) : helper)))
    + "</li>\n          <li>Ingredients: "
    + alias4(((helper = (helper = helpers.ingredients || (depth0 != null ? depth0.ingredients : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"ingredients","hash":{},"data":data}) : helper)))
    + "</li>\n          <li>Publisher: "
    + alias4(((helper = (helper = helpers.publisher || (depth0 != null ? depth0.publisher : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"publisher","hash":{},"data":data}) : helper)))
    // + "</li>\n       </ul>\n    <p><a class=\"btn btn-default\" href=\"#\" role=\"button\">Detail & Image &raquo;</a></p>\n  </div>\n</div>";
},"useData":true});
templates['recipe_list'] = template({"1":function(container,depth0,helpers,partials,data) {
    var helper, alias1=depth0 != null ? depth0 : {}, alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "    <div class=\"row\">\n      <div class=\"col-md-12 recipe\" id=\""
    + alias4(((helper = (helper = helpers.pk || (depth0 != null ? depth0.pk : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"pk","hash":{},"data":data}) : helper)))
    + "\">\n        <h2 id=\""
    + alias4(((helper = (helper = helpers.pk || (depth0 != null ? depth0.pk : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"pk","hash":{},"data":data}) : helper)))
    + "\">Title:"
    + alias4(((helper = (helper = helpers.title || (depth0 != null ? depth0.title : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"title","hash":{},"data":data}) : helper)))
    + "</h2>\n        <p><a class=\"btn btn-default\" href=\"#\" role=\"button\">View details &raquo;</a></p>\n      </div>\n    </div>\n";
},"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers.each.call(depth0 != null ? depth0 : {},(depth0 != null ? depth0.recipes : depth0),{"name":"each","hash":{},"fn":container.program(1, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"useData":true});
templates['nav_list'] = template({"1":function(container,depth0,helpers,partials,data) {
    var alias1=container.lambda, alias2=container.escapeExpression;

  return "  <li><a class=\"letter\" id=\""
    + alias2(alias1(depth0, depth0))
    + "\" href=\"#\">"
    + alias2(alias1(depth0, depth0))
    + "</a></li>\n";
},"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers.each.call(depth0 != null ? depth0 : {},(depth0 != null ? depth0.letters : depth0),{"name":"each","hash":{},"fn":container.program(1, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"useData":true});
templates['pagination'] = template({"1":function(container,depth0,helpers,partials,data) {
    var stack1, helper, alias1=depth0 != null ? depth0 : {}, alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "    <span class=\"step-links\">\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.previous_page : depth0),{"name":"if","hash":{},"fn":container.program(2, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n            <span class=\"current\">\n                Page "
    + alias4(((helper = (helper = helpers.current_page || (depth0 != null ? depth0.current_page : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"current_page","hash":{},"data":data}) : helper)))
    + " of "
    + alias4(((helper = (helper = helpers.all_pages || (depth0 != null ? depth0.all_pages : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"all_pages","hash":{},"data":data}) : helper)))
    + ".\n            </span>\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.next_page : depth0),{"name":"if","hash":{},"fn":container.program(4, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "    </span>\n";
},"2":function(container,depth0,helpers,partials,data) {
    var helper;

  return "            <a id='"
    + container.escapeExpression(((helper = (helper = helpers.previous_page || (depth0 != null ? depth0.previous_page : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : {},{"name":"previous_page","hash":{},"data":data}) : helper)))
    + "' class=\"page-button\" href='#'>previous</a>\n";
},"4":function(container,depth0,helpers,partials,data) {
    var helper;

  return "            <a id='"
    + container.escapeExpression(((helper = (helper = helpers.next_page || (depth0 != null ? depth0.next_page : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : {},{"name":"next_page","hash":{},"data":data}) : helper)))
    + "' class=\"page-button\" href=\"#\">next</a>\n";
},"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers["if"].call(depth0 != null ? depth0 : {},(depth0 != null ? depth0.recipes : depth0),{"name":"if","hash":{},"fn":container.program(1, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"useData":true});
})();
