"use strict";
var RenderUrlsToFile, system;

system = require("system");

RenderUrlsToFile = function(params, callbackPerUrl, callbackFinal) {
    var getFilename, page, retrieve, webpage;
    webpage = require("webpage");
    page = null;
    getFilename = function(name) {
        return "data/png/" + name + ".png";
    };
    retrieve = function() {
        page = webpage.create();
        page.viewportSize = {
            width: 800,
            height: 600
        };
        page.settings.userAgent = "Phantom.js bot";
        var url;
        if (/^https?:\/\//.test(params.url)) {
            url = params.url;
        } else {
            url = 'http://' + params.url;
        }
        return page.open(url, function(status) {
            console.log(status);
            var file = getFilename(params.name);
            if (status === "success") {
                console.log(file);
                page.render(file);
            }
            page.close();
            return callbackFinal();
        });
    };
    return retrieve();
};

var params = {};
var regexp = /^([^=]+)=([^$]+)/;

system.args.forEach(function(arg) {
  var parts = arg.match(regexp);
  if (!parts) { return; }
  params[parts[1]] = parts[2];
});

RenderUrlsToFile(params, (function(status, url, file) {
    if (status !== "success") {
        return console.log("Unable to render '" + url + "'");
    } else {
        return console.log("Rendered '" + url + "' at '" + file + "'");
    }
}), function() {
    return phantom.exit();
});
