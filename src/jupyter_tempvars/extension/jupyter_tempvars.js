/**
 * jupyter_tempvars.js
 *
 * Wrap all code in suitable tagged code cells with a
 * tempvars.TempVars context manager to handle temporary variables.
 *
 * Code-patching implementation adapted from the execution_dependencies
 * Jupyter extension:
 *
 *  https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/execution_dependencies
 *
 * Event-based import of TempVars on kernel_ready adapted from jupyter-black:
 *
 *  https://github.com/drillan/jupyter-black/blob/d197945508a9d2879f2e2cc99cafe0cedf034cf2/kernel_exec_on_cell.js#L347
 *
 *
 * @author  Brian Skinn, https://github.com/bskinn
 *
 */

define([
  'base/js/namespace',
  'base/js/events',
  'notebook/js/codecell'
], function (Jupyter, events, codecell) {

    "use strict";

    /*
     * Initializing useful things.
     */
    var CodeCell = codecell.CodeCell
    var c_log = (msg) => {console.log(`[jupyter-tempvars] ${msg}`);};
    const is_tempvars = (tag) => tag.startsWith("tempvars");
    const indent_str = "    "

    return {
        load_ipython_extension: function () {
            /*
             *  We need to import _TempVars afresh every time the kernel (re)starts
             */
            c_log('adding TempVars import upon kernel_ready event')
            events.on("kernel_ready.Kernel", function(evt, data) {
                c_log("importing _TempVars");
                Jupyter.notebook.kernel.execute("from tempvars import TempVars as _TempVars");
            });

            /*
             * Logic for patching a cell's code with _TempVars
             */
            var format_starts = function (tags) {
                var starts = []

                tags.forEach( tag => {
                    if ( tag.startsWith("tempvars-start-") ) { starts.push(tag.substring(15)); }
                });

                return (starts.length == 0 ? "" : 'starts=["' + starts.join('", "') + '"]');
            }

            var format_ends = function (tags) {
                var ends = []

                tags.forEach( tag => {
                    if ( tag.startsWith("tempvars-end-") ) { ends.push(tag.substring(13)); }
                });

                return (ends.length == 0 ? "" : 'ends=["' + ends.join(':, "') + '"]');
            }

            var construct_context_mgr = function (tags) {
                var start = format_starts(tags);
                var end = format_ends(tags);

                var args = [];

                if ( start.length > 0 ) { args.push(start); }
                if ( end.length > 0 ) { args.push(end); }

                if ( args.length == 0 ) { return ""; }

                return `with _TempVars(${args.join(", ")}):\n`;
            }

            var modify_code = function (orig_text, tags) {
                // No change if code block is empty
                if ( orig_text.length == 0 ) { return orig_text; }

                var ctx_mgr = construct_context_mgr(tags);

                if (ctx_mgr.length == 0 ) {
                    return orig_text;
                } else {
                    return ctx_mgr + indent_str + orig_text.replaceAll("\n", `\n${indent_str}`);
                }
            }

            /*
             * Patch the CodeCell execution
            */

            c_log('patching CodeCell.execute');
            var orig_execute = CodeCell.prototype.execute;

            CodeCell.prototype.execute = function (stop_on_error) {
                var tags = this.metadata.tags || [];  // Could do this by inspecting first line of cell text, too

                if (tags.some(is_tempvars)) {
                    var orig_text = this.get_text();
                    var new_text = modify_code(orig_text, tags);

                    this.set_text(new_text);
                    orig_execute.call(this, stop_on_error);
                    this.set_text(orig_text);
                } else {
                    orig_execute.call(this, stop_on_error);
                }
            };
        }
    };
});
