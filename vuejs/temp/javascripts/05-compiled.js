"use strict";

var childModule = {};

childModule.install = function (Vue, options) {
  Vue.component("child", {
    render: function render(h) {

      return h(
        "div",
        {
          attrs: { level: 1 }
        },
        [h("span", ["Hello"]), " world"]
      );
    }
  });
};
