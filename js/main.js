var pmApp = angular.module('pmApp', ['ui.materialize']);

pmApp.controller('mainCtrl', function ($scope, $http, $timeout) {

  $http.get('json/dali.json').success(function(data) {
    data = data.replace('PM2.5','PM2p5');
    data = JSON.parse(data);
    window.data = data;
    $scope.datas = data;
  });
});

pmApp.filter('color',function() {
  return function(pm25) {
    if (pm25>0) 
      if (pm25<12)
        return '#9CFF9C'
      else if (pm25<24)
        return '#31FF00'
      else if (pm25<36)
        return '#31CF00'
      else if (pm25<42)
        return '#FFFF00'
      else if (pm25<48)
        return '#FFCF00'
      else if (pm25<54)
        return '#FF9A00'
      else if (pm25<59)
        return '#FF6464'
      else if (pm25<65)
        return '#FF0000'
      else if (pm25<71)
        return '#900'
      else
        return '#CE30FF';
    else
      return 'white';
  };
});
