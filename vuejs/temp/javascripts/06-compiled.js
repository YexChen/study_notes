"use strict";

var elementNumbers = {};

elementNumbers.install = function (Vue, options) {
  Vue.component("elNumbers", {
    render: function render(h) {
      var _this = this;

      return h(
        "div",
        { "class": this.size },
        [h(
          "button",
          {
            on: {
              "click": this.minus
            }
          },
          ["-"]
        ), h("input", {
          on: {
            "input": function input(e) {
              return _this.sync("cValue", parseInt(e.target.value));
            }
          },
          domProps: {
            "value": this.cValue
          }
        }), h(
          "button",
          {
            on: {
              "click": this.add
            }
          },
          ["+"]
        )]
      );
    },
    props: {
      value: { type: Number, default: 0 },
      min: { type: Number, default: Infinity * -1 },
      max: { Number: Number, default: Infinity },
      step: { type: Number, default: 1 },
      size: { String: String, default: "large" },
      disabled: { type: Boolean, default: false }
    },
    data: function data() {
      return {
        cValue: this.value,
        cDisabled: this.passDisabled
      };
    },
    watch: {
      cValue: function cValue(newVal, oldVal) {
        if (newVal < this.min) this.cValue = this.min;else if (newVal > this.max) this.cValue = this.max;
      }
    },
    methods: {
      add: function add() {
        this.cValue += this.step;
      },
      minus: function minus() {
        this.cValue -= this.step;
      },
      sync: function sync(prop, value) {
        console.log("sync");
        this[prop] = value;
      }
    }
  });
};
