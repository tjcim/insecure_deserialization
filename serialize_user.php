<?php
class User{
    public $username;
    public $status;

    function __wakeup() {
      echo shell_exec('ls -la');
    }

    function __destruct() {
      echo shell_exec('whoami');
    }

    function __toString() {
      return shell_exec('echo $(hostname)');
    }

    function __call($name, $args) {
      echo shell_exec('ping -c 1 127.0.0.1');
    }
}
$user = new User;
$user->username = 'vickie';
$user->status = 'not admin';
$serialized_string = serialize($user);
echo "*** Serialized user:\n" . $serialized_string . "\n";
echo "\n*** Executing the wakeup magic function\n";
$unserialized_data = unserialize($serialized_string);
echo "\n*** Unserialized user:\n";
echo var_dump($unserialized_data);
echo var_dump($unserialized_data->status);
echo "\n*** Executing the toString magic funciton\n";
echo $unserialized_data;
echo "\n*** Executing the call magic funciton\n";
$unserialized_data->undefined();
echo "\n*** Executing the destruct magic funciton\n";
?>
