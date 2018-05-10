myApp = angular.module('myApp', ['ngRoute']);
myApp.factory('AuthService',
  ['$q', '$timeout', '$http',
  function ($q, $timeout, $http) {

    // create user variable
    var user = null;

function login(email, password) {

  // create a new instance of deferred
  var deferred = $q.defer();

  // send a post request to the server
  $http.post('/api/login', {email: email, password: password})
    // handle success
    .then(function (response) {
      if(response.status === 200 && response.data['result']==true){
        user = true;
        deferred.resolve();
      } else {
        user = false;
        deferred.reject();
      }
    })
    // handle error
    .catch(function (data) {
      user = false;
      deferred.reject();
    });

  // return promise object
  return deferred.promise;

}

function register(email, username, password, password_confirm) {

  // create a new instance of deferred
  var deferred = $q.defer();

  // send a post request to the server
  $http.post('/api/register', {email: email, username: username, password: password, password_confirm: password_confirm})
    // handle success
    .then(function (response) {
      if(response.status === 200 && response.data['result']=='success'){
        deferred.resolve();
      } else {
        demo.regFailed('top', 'center', response.data['result']);
        deferred.reject();
      }
    })
    // handle error
    .catch(function (response) {
      deferred.reject();
    });

  // return promise object
  return deferred.promise;

}

function isLoggedIn() {
  if(user) {
    return true;
  } else {
    return false;
  }
}

function getUserName() {
  return $http.get('/api/username');
}

function logout(username) {

  // create a new instance of deferred
  var deferred = $q.defer();

  // send a get request to the server
  $http.get('/api/username')
    .then(function (response) {
      if(response.data['username']){
        $http.get('/api/logout')
          // handle success
          .then(function (_response) {
            demo.logoutSuccess('top','center', response.data['username']);
            user = false;
            deferred.resolve();
          },
          // handle error
          function (_response) {
            demo.logoutSuccess('top','center', response.data['username']);
            user = false;
            deferred.reject();
          });  
      }
    })
    .catch(function (response) {
    })


  // return promise object
  return deferred.promise;

}

function getUserStatus() {
  return $http.get('/api/status')
  // handle success
  .then(function (response) {
    if(response.data['status']){
      user = true;
    } else {
      user = false;
    }
  },
  // handle error
  function (response) {
    user = false;
  });
}

    // return available functions for use in controllers
    return ({
      isLoggedIn: isLoggedIn,
      login: login,
      logout: logout,
      register: register,
      getUserStatus: getUserStatus
    });

}]);

