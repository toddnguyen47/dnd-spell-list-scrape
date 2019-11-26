function ShowSpellDescription() {
  this.prevElem = null;

  this.preventClickSelect = function(e, selector) {
    selector.mousedown(function(e) {
      e.preventDefault();
    });
  };

  this.invoke = function() {
    this.attachClickHandler();
  };

  this.hideElem = function(selector) {
    selector
      .find("div[class*='spell-description'")
      .eq(0)
      .hide();
  };

  /** Ref: https://www.w3schools.com/howto/howto_js_copy_clipboard.asp */
  this.copyToClipboard = function(elem) {
    t = elem.text();
    navigator.clipboard.writeText(t);
  };

  this.toggleElem = function(selector) {
    let e = selector.find("div[class*='spell-description'").eq(0);
    e.toggle();
    this.copyToClipboard(e);
  };

  this.elemsNotEqual = function(selector1, selector2) {
    // Ref: https://stackoverflow.com/a/2647888
    return selector1 != null && selector2 != null && false === $(selector1).is(selector2);
  };

  this.attachClickHandler = function() {
    let self = this;
    $(".table__td-spell-name").click(function(e) {
      self.preventClickSelect(e, $(this));

      // Ref: https://stackoverflow.com/a/2647888
      if (self.elemsNotEqual(self.prevElem, $(this))) self.hideElem(self.prevElem);

      self.toggleElem($(this));
      self.prevElem = $(this);
    });
  };
}

$(document).ready(function() {
  let showSpellDesc = new ShowSpellDescription();
  showSpellDesc.invoke();
});
