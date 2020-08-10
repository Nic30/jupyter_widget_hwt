var widgets = require('@jupyter-widgets/base');

var d3 = require('d3');
var d3_wave = require('d3-wave');
d3.WaveGraph = d3_wave.WaveGraph;
var _ = require('lodash');

// See signal_dump.py for the kernel counterpart to this file.


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
function serializeSignalDataWithoutRenderes(d, model) {
	var t = d.type;
	var copy = { ...d };
	var tCopy = { ...t };
	delete tCopy["renderer"];
	delete tCopy["formatter"];
	// do save only name of the formater instead of it's value
	copy.type = tCopy;
	var ren = t.renderer;
	if (t.formatter && ren && t.formatter !== ren.DEFAULT_FORMATTER) {
		for (var key in ren.FORMATTERS) {
			if (ren.FORMATTERS.hasOwnProperty(key)) {
				if (t.formatter === ren.FORMATTERS[key]) {
					tCopy.formatter = key;
					break;
				}
			}
		}
	}
	if (d.children) {
		copy.children = d.children.map(serializeSignalDataWithoutRenderes);
	}
	if (d._children) {
		copy._children = d._children.map(serializeSignalDataWithoutRenderes);
	}

	return copy;
}

// When serializing the entire widget state for embedding, only values that
// differ from the defaults will be specified.
var HwtSignalDumpModel = widgets.DOMWidgetModel.extend({
	defaults: _.extend({}, widgets.DOMWidgetModel.prototype.defaults(), {
		_model_name: 'HwtSignalDumpModel',
		_view_name: 'HwtSignalDumpView',
		_model_module: 'jupyter_widget_hwt',
		_view_module: 'jupyter_widget_hwt',
		_model_module_version: '0.0.1',
		_view_module_version: '0.0.1',
		signal_data: {},
		width: "800px",
		height: "250px"

	}),
}, {
	serializers: _.extend({
		signal_data: { serialize: serializeSignalDataWithoutRenderes }
	}, widgets.DOMWidgetModel.serializers)
});

//class HwtSignalDumpModel extends widgets.WidgetModel {
//	defaults() {
//		return {
//			...super.defaults(),
//			_model_name: 'HwtSignalDumpModel',
//			_view_name: 'HwtSignalDumpView',
//			_model_module: 'jupyter_widget_hwt',
//			_view_module: 'jupyter_widget_hwt',
//			_model_module_version: '0.0.1',
//			_view_module_version: '0.0.1',
//			signal_data: {},
//			width: "800px",
//			height: "250px"
//		}
//	}
//
//	static serializers = {
//		...widgets.DOMWidgetModel.serializers,
//		signal_data: { serialize: serializeSignalDataWithoutRenderes },
//	}
//}


// Custom View. Renders the widget model.
var HwtSignalDumpView = widgets.DOMWidgetView.extend({
	// Defines how the widget gets rendered into the DOM
	render: function() {
		this.value_changed();

		// Observe changes in the value traitlet in Python, and define
		// a custom callback.
		this.model.on('change:signal_data', this.value_changed, this);
	},

	value_changed: function() {
		var root = d3.select(this.el);
		root.selectAll("svg").remove();
		var width = this.model.get('width');
		var height = this.model.get('height');
		var svg = root.append("svg")
			.attr("class", "wave-graph")
			.attr("width", width)
			.attr("height", height)

		var g = new d3.WaveGraph(svg);
		var signalData = this.model.get('signal_data');
		g.bindData(signalData);
		g.draw();
	}
});


module.exports = {
	HwtSignalDumpModel: HwtSignalDumpModel,
	HwtSignalDumpView: HwtSignalDumpView
};
