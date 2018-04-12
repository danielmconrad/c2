var raceEthnicityRowSelector = '.user-race-ethnicity-inline .form-row';
var inputsSelector = 'select';

(function($) {

  // Disable any other field in a row if one of the fields is populated
  var defineRowBehavior = function($row) {
    var fields = $row.find(inputsSelector);

    fields.on('change', function() {
      var hasValue = !!$(this).val();
      fields.not(this).prop('disabled', hasValue).addClass('disabled', hasValue);
    });
  };

  // Make sure any dynamically added rows behave the same way
  $(document).on('formset:added', function(event, $row, formsetName) {
    if (formsetName == 'userraceethnicity_set') {
      defineRowBehavior($row)
    }
  });

  // Find any rows already on the page
  $(function(){
    $(raceEthnicityRowSelector).each(function() {
      defineRowBehavior($(this));
    });
  });

})(window.jQuery || django.jQuery);
