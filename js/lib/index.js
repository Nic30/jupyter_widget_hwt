// Export widget models and views, and the npm package version number.
var scheme = require('./scheme/scheme.js');
var signal_dump = require('./signal_dump/signal_dump.js');

module.exports = {
	    HwtSchemeModel: scheme.HwtSchemeModel,
	    HwtSchemeView: scheme.HwtSchemeView,
	    HwtSignalDumpModel: signal_dump.HwtSignalDumpModel,
	    HwtSignalDumpView: signal_dump.HwtSignalDumpView
}
module.exports['version'] = require('../package.json').version;
