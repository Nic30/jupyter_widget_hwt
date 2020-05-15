var plugin = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'jupyter_widget_hwt',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'jupyter_widget_hwt',
          version: plugin.version,
          exports: plugin
      });
  },
  autoStart: true
};

