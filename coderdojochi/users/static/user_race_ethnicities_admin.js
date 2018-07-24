var raceEthnicityRowSelector = '.user-race-ethnicity-inline .form-row';
var inputsSelector = 'select';

(function ($) {
  // Sets the current and change behavior for a row
  var defineRowBehavior = function (rowElem) {
    var fields = $(rowElem).find(inputsSelector);

    fields
      .on('change', function () { disableSiblings(fields, this); })
      .filter(function (i, elem) { return $(elem).val(); })
      .each(function (i, elem) { disableSiblings(fields, elem); });
  };

  // jQuery function that find sibling fields and disables them
  var disableSiblings = function (fields, fieldElem) {
    var hasValue = !!$(fieldElem).val();
    fields
      .not(fieldElem)
      .prop('disabled', hasValue)
      .addClass('disabled', hasValue);
  };

  // Make sure any dynamically added rows behave the same way
  $(document).on('formset:added', function (event, $row, formsetName) {
    if (formsetName == 'raceethnicity_set') {
      $row.find(inputsSelector).on('change', disableSiblings);
    }
  });

  // Find any rows already on the page
  $(function () {
    $(raceEthnicityRowSelector)
      .each(function (i, rowElem) { defineRowBehavior(rowElem); });
  });

})(window.jQuery || django.jQuery);
