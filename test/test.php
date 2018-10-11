<?php

$orgName = "YOUR_ORGANZATION";

$username = "YOUR_USERNAME";

$token = "YOUR_TOKEN";

$key = md5($username);

$cryptAlgo = 'AES-256-CFB';

$iv = mb_substr(base64_decode($token), 0, 16, '8bit');
echo $iv.openssl_encrypt($token, $cryptAlgo, $key, 0, $iv);
$secret = base64_encode($iv.openssl_encrypt($token, $cryptAlgo, $key, 0, $iv));

date_default_timezone_set('UTC');

$current_time = date('c');

$nonce = md5(rand(), true);

$base64_nonce = base64_encode($nonce);

$password_digest = base64_encode(sha1($nonce . $current_time . $secret, true));
echo "passwprd digest\"$password_digest\"\n";
$header = "UsernameToken Username=\"$username\",".

"PasswordDigest=\"$password_digest\",".

"Nonce=\"$base64_nonce\",".

"Created=\"$current_time\",".

"Organization=\"$orgName\"";

echo $header;

echo $iv;
?>