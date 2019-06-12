all about php:

1. php中　system($_GET['c']); 可以运行系统命令
2. php type juggling, "==" 比较的是2个数的
<?php
echo intval('0e548' == '0e547'); // result 1, which means TRUE
echo intval('0e548' === '0e547'); // result 0, which means FALSE
?>
3. 
