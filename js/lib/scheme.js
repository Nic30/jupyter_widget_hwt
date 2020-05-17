var widgets = require('@jupyter-widgets/base');
var scheme_css = require('./scheme.css');

var d3 = require('d3');
d3.HwSchematic = require('d3-hwschematic').HwSchematic;
var _ = require('lodash');

// See example.py for the kernel counterpart to this file.


// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including
//
//  - `_view_name`
//  - `_view_module`
//  - `_view_module_version`
//
//  - `_model_name`
//  - `_model_module`
//  - `_model_module_version`
//
//  when different from the base class.

// When serialiazing the entire widget state for embedding, only values that
// differ from the defaults will be specified.
var HwtSchemeModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'HwtSchemeModel',
        _view_name : 'HwtSchemeView',
        _model_module : 'jupyter_widget_hwt',
        _view_module : 'jupyter_widget_hwt',
        _model_module_version : '0.0.1',
        _view_module_version : '0.0.1',
        value : {},
        width : "800px",
        height : "250px"

    })
});


// Custom View. Renders the widget model.
var HwtSchemeView = widgets.DOMWidgetView.extend({
    // Defines how the widget gets rendered into the DOM
    render: function() {
        this.value_changed();

        // Observe changes in the value traitlet in Python, and define
        // a custom callback.
        this.model.on('change:value', this.value_changed, this);
    },

    value_changed: function() {
	    var root = d3.select(this.el);
	    root.selectAll("svg").remove();
        var width = this.model.get('width');
        var height = this.model.get('height');
        var svg = root.append("svg")
            .attr("width", width)
            .attr("height",  height);

        var g = new d3.HwSchematic(svg);
        var zoom = d3.zoom();
        zoom.on("zoom", function applyTransform() {
            g.root.attr("transform", d3.event.transform)
        });
        
        // disable zoom on doubleclick 
        // because it interferes with component expanding/collapsing
        svg.call(zoom)
           .on("dblclick.zoom", null)

        var graph = this.model.get('value');
        // deepcopy
        graph = JSON.parse(JSON.stringify(graph));
        g.bindData(graph);
    }
});


module.exports = {
    HwtSchemeModel: HwtSchemeModel,
    HwtSchemeView: HwtSchemeView
};
