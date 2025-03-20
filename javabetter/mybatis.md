# MyBatisé¢è¯•é¢˜ï¼Œ23é“MyBatiså…«è‚¡æ–‡ï¼ˆ6åƒå­—30å¼ æ‰‹ç»˜å›¾ï¼‰ï¼Œé¢æ¸£é€†è¢­å¿…çœ‹ğŸ‘ | äºŒå“¥çš„Javaè¿›é˜¶ä¹‹è·¯

源地址：[https://javabetter.cn/sidebar/sanfene/mybatis.html](https://javabetter.cn/sidebar/sanfene/mybatis.html)

# MyBatisé¢è¯•é¢˜ï¼Œ23é“MyBatiså…«è‚¡æ–‡ï¼ˆ6åƒå­—30å¼
æ‰‹ç»˜å›¾ï¼‰ï¼Œé¢æ¸£é€†è¢­å¿…çœ‹ğŸ‘

ä¸‰åˆ†æ¶é¢æ¸£é€†è¢­é¢æ¸£é€†è¢­çº¦ 10455 å­—å¤§çº¦ 35 åˆ†é’Ÿ

* * *

æ­¤é¡µå†…å®¹

  * åŸºç¡€
  *     * 1\. è¯´è¯´ä»€ä¹ˆæ˜¯ MyBatis?
    * 2\. Hibernate å’Œ MyBatis æœ‰ä»€ä¹ˆåŒºåˆ«ï¼Ÿ
    * 3\. MyBatis ä½¿ç”¨è¿‡ç¨‹ï¼Ÿç”Ÿå‘½å‘¨æœŸï¼Ÿ
    * 4\. åœ¨ mapper ä¸­å¦‚ä½•ä¼ é€’å¤šä¸ªå‚æ•°ï¼Ÿ
    * 5\. å®ä½“ç±»å±æ€§åå’Œè¡¨ä¸­å­—æ®µåä¸ä¸€æ · ï¼Œæ€ä¹ˆåŠ?
    * 6\. Mybatis æ˜¯å¦å¯ä»¥æ˜ å°„ Enum æšä¸¾ç±»ï¼Ÿ
    * 7\. #{}å’Œ${}çš„åŒºåˆ«?
    * 8\. æ¨¡ç³ŠæŸ¥è¯¢ like è¯­å¥è¯¥æ€ä¹ˆå†™?
    * 9\. Mybatis èƒ½æ‰§è¡Œä¸€å¯¹ä¸€ã€ä¸€å¯¹å¤šçš„å…³è”æŸ¥è¯¢å—ï¼Ÿ
    * 10\. Mybatis æ˜¯å¦æ”¯æŒå»¶è¿ŸåŠ è½½ï¼ŸåŸç†ï¼Ÿ
    * 11\. å¦‚ä½•è·å–ç”Ÿæˆçš„ä¸»é”®?
    * 12\. MyBatis æ”¯æŒåŠ¨æ€ SQL å—ï¼Ÿ
    * 13\. MyBatis å¦‚ä½•æ‰§è¡Œæ‰¹é‡æ“ä½œï¼Ÿ
    * 14\. è¯´è¯´ Mybatis çš„ä¸€çº§ã€äºŒçº§ç¼“å­˜ï¼Ÿ
  * åŸç†
  *     * 15\. èƒ½è¯´è¯´ MyBatis çš„å·¥ä½œåŸç†å—ï¼Ÿ
    * 16\. MyBatis çš„åŠŸèƒ½æ¶æ„æ˜¯ä»€ä¹ˆæ ·çš„ï¼Ÿ
    * 17\. ä¸ºä»€ä¹ˆ Mapper æ¥å£ä¸éœ€è¦å®ç°ç±»ï¼Ÿ
    * 18.Mybatis éƒ½æœ‰å“ªäº› Executor æ‰§è¡Œå™¨ï¼Ÿ
  * æ’ä»¶
  *     * 19\. è¯´è¯´ Mybatis çš„æ’ä»¶è¿è¡ŒåŸç†ï¼Œå¦‚ä½•ç¼–å†™ä¸€ä¸ªæ’ä»¶ï¼Ÿ
    * 20\. MyBatis æ˜¯å¦‚ä½•è¿›è¡Œåˆ†é¡µçš„ï¼Ÿåˆ†é¡µæ’ä»¶çš„åŸç†æ˜¯ä»€ä¹ˆï¼Ÿ
  * è¡¥å……
  *     * 21.è¯´è¯´ JDBC çš„æ‰§è¡Œæ­¥éª¤ï¼Ÿ
    * 22.åˆ›å»ºè¿æ¥æ‹¿åˆ°çš„æ˜¯ä»€ä¹ˆå¯¹è±¡ï¼Ÿ
    * 23.Statement ä¸ PreparedStatement çš„åŒºåˆ«
    * 24\. ä»€ä¹ˆæ˜¯ SQL æ³¨å…¥ï¼Ÿå¦‚ä½•é˜²æ­¢ SQL æ³¨å…¥ï¼Ÿ

6400 å­— 30 å¼ æ‰‹ç»˜å›¾ï¼Œè¯¦è§£ 23 é“ MyBatis
é¢è¯•é«˜é¢‘é¢˜ï¼ˆè®©å¤©ä¸‹æ²¡æœ‰éš¾èƒŒçš„å…«è‚¡ï¼‰ï¼Œé¢æ¸£èƒŒä¼šè¿™äº› MyBatis
å…«è‚¡æ–‡ï¼Œè¿™æ¬¡åŠæ‰“é¢è¯•å®˜ï¼Œæˆ‘è§‰å¾—ç¨³äº†ï¼ˆæ‰‹åŠ¨
dogï¼‰ã€‚æ•´ç†ï¼šæ²‰é»˜ç‹äºŒï¼Œæˆ³[è½¬è½½é“¾æ¥](https://mp.weixin.qq.com/s/en2RgcVx52Ql3tYGLfv3Kw)ï¼Œä½œè€…ï¼šä¸‰åˆ†æ¶ï¼Œæˆ³[åŸæ–‡é“¾æ¥](https://mp.weixin.qq.com/s/O_5Id2o9IP4loPazJuiHng)ã€‚

å¤§å®¶å¥½ï¼Œæˆ‘æ˜¯äºŒå“¥å‘€ï¼Œé¢æ¸£é€†è¢­ç³»åˆ—ç»§ç»­ï¼Œè¿™èŠ‚æˆ‘ä»¬çš„ä¸»è§’æ˜¯
MyBatisï¼Œä½œä¸ºå½“å‰å›½å†…æœ€æµè¡Œçš„ ORM æ¡†æ¶ï¼Œæ˜¯æˆ‘ä»¬è¿™äº› crud
é€‰æ‰‹æœ€è¶æ‰‹çš„å·¥å…·ï¼Œèµ¶ç´§æ¥çœ‹çœ‹é¢è¯•éƒ½ä¼šé—®å“ªäº›é—®é¢˜å§ã€‚

## åŸºç¡€

### 1\. è¯´è¯´ä»€ä¹ˆæ˜¯ MyBatis?

![MyBatis
logo](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-41c60cf7-6551-4720-8735-290a083640a5.png)MyBatis
logo

**å…ˆå¹ä¸€ä¸‹** ï¼š

  * Mybatis æ˜¯ä¸€ä¸ªåŠ ORMï¼ˆå¯¹è±¡å…³ç³»æ˜ å°„ï¼‰æ¡†æ¶ï¼Œå®ƒå†…éƒ¨å°è£…äº† JDBCï¼Œå¼€å‘æ—¶åªéœ€è¦å…³æ³¨ SQL è¯­å¥æœ¬èº«ï¼Œä¸éœ€è¦èŠ±è´¹ç²¾åŠ›å»å¤„ç†åŠ è½½é©±åŠ¨ã€åˆ›å»ºè¿æ¥ã€åˆ›å»º statement ç­‰ç¹æ‚çš„è¿‡ç¨‹ã€‚ç¨‹åºå‘˜ç›´æ¥ç¼–å†™åŸç”Ÿæ€ sqlï¼Œå¯ä»¥ä¸¥æ ¼æ§åˆ¶ sql æ‰§è¡Œæ€§èƒ½ï¼Œçµæ´»åº¦é«˜ã€‚
  * MyBatis å¯ä»¥ä½¿ç”¨ XML æˆ–æ³¨è§£æ¥é…ç½®å’Œæ˜ å°„åŸç”Ÿä¿¡æ¯ï¼Œå°† POJO æ˜ å°„æˆæ•°æ®åº“ä¸­çš„è®°å½•ï¼Œé¿å…äº†å‡ ä¹æ‰€æœ‰çš„ JDBC ä»£ç å’Œæ‰‹åŠ¨è®¾ç½®å‚æ•°ä»¥åŠè·å–ç»“æœé›†ã€‚

**å†è¯´ä¸€ä¸‹ç¼ºç‚¹**

  * SQL è¯­å¥çš„ç¼–å†™å·¥ä½œé‡è¾ƒå¤§ï¼Œå°¤å…¶å½“å­—æ®µå¤šã€å…³è”è¡¨å¤šæ—¶ï¼Œå¯¹å¼€å‘äººå‘˜ç¼–å†™ SQL è¯­å¥çš„åŠŸåº•æœ‰ä¸€å®šè¦æ±‚
  * SQL è¯­å¥ä¾èµ–äºæ•°æ®åº“ï¼Œå¯¼è‡´æ•°æ®åº“ç§»æ¤æ€§å·®ï¼Œä¸èƒ½éšæ„æ›´æ¢æ•°æ®åº“

#### ORM æ˜¯ä»€ä¹ˆ?

![ORMç®€å•ç¤ºæ„å›¾](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-
ea212850-56e0-4d12-98fb-03bb40007f44.png)ORMç®€å•ç¤ºæ„å›¾

  * ORMï¼ˆObject Relational Mappingï¼‰ï¼Œå¯¹è±¡å…³ç³»æ˜ å°„ï¼Œæ˜¯ä¸€ç§ä¸ºäº†è§£å†³å…³ç³»å‹æ•°æ®åº“æ•°æ®ä¸ç®€å• Java å¯¹è±¡ï¼ˆPOJOï¼‰çš„æ˜ å°„å…³ç³»çš„æŠ€æœ¯ã€‚ç®€å•æ¥è¯´ï¼ŒORM æ˜¯é€šè¿‡ä½¿ç”¨æè¿°å¯¹è±¡å’Œæ•°æ®åº“ä¹‹é—´æ˜ å°„çš„å…ƒæ•°æ®ï¼Œå°†ç¨‹åºä¸­çš„å¯¹è±¡è‡ªåŠ¨æŒä¹…åŒ–åˆ°å…³ç³»å‹æ•°æ®åº“ä¸­ã€‚

#### ä¸ºä»€ä¹ˆè¯´ Mybatis æ˜¯åŠè‡ªåŠ¨ ORM æ˜
å°„å·¥å…·ï¼Ÿå®ƒä¸å…¨è‡ªåŠ¨çš„åŒºåˆ«åœ¨å“ªé‡Œï¼Ÿ

  * Hibernate å±äºå…¨è‡ªåŠ¨ ORM æ˜ å°„å·¥å…·ï¼Œä½¿ç”¨ Hibernate æŸ¥è¯¢å…³è”å¯¹è±¡æˆ–è€…å…³è”é›†åˆå¯¹è±¡æ—¶ï¼Œå¯ä»¥æ ¹æ®å¯¹è±¡å…³ç³»æ¨¡å‹ç›´æ¥è·å–ï¼Œæ‰€ä»¥å®ƒæ˜¯å…¨è‡ªåŠ¨çš„ã€‚
  * è€Œ Mybatis åœ¨æŸ¥è¯¢å…³è”å¯¹è±¡æˆ–å…³è”é›†åˆå¯¹è±¡æ—¶ï¼Œéœ€è¦æ‰‹åŠ¨ç¼–å†™ SQL æ¥å®Œæˆï¼Œæ‰€ä»¥ï¼Œè¢«ç§°ä¹‹ä¸ºåŠè‡ªåŠ¨ ORM æ˜ å°„å·¥å…·ã€‚

#### JDBC ç¼–ç¨‹æœ‰å“ªäº›ä¸è¶³ä¹‹å¤„ï¼ŒMyBatis æ˜¯å¦‚ä½•è§£å†³çš„ï¼Ÿ

![JDBCç¼–ç¨‹çš„ä¸è¶³](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-f8b181a3-ad40-4381-98ba-351668579bfb.png)JDBCç¼–ç¨‹çš„ä¸è¶³

  * 1ã€æ•°æ®è¿æ¥åˆ›å»ºã€é‡Šæ”¾é¢‘ç¹é€ æˆç³»ç»Ÿèµ„æºæµªè´¹ä»è€Œå½±å“ç³»ç»Ÿæ€§èƒ½ï¼Œåœ¨ mybatis-config.xml ä¸­é…ç½®æ•°æ®é“¾æ¥æ± ï¼Œä½¿ç”¨è¿æ¥æ± ç»Ÿä¸€ç®¡ç†æ•°æ®åº“è¿æ¥ã€‚
  * 2ã€sql è¯­å¥å†™åœ¨ä»£ç ä¸­é€ æˆä»£ç ä¸æ˜“ç»´æŠ¤ï¼Œå°† sql è¯­å¥é…ç½®åœ¨ XXXXmapper.xml æ–‡ä»¶ä¸­ä¸ java ä»£ç åˆ†ç¦»ã€‚
  * 3ã€å‘ sql è¯­å¥ä¼ å‚æ•°éº»çƒ¦ï¼Œå› ä¸º sql è¯­å¥çš„ where æ¡ä»¶ä¸ä¸€å®šï¼Œå¯èƒ½å¤šä¹Ÿå¯èƒ½å°‘ï¼Œå ä½ç¬¦éœ€è¦å’Œå‚æ•°ä¸€ä¸€å¯¹åº”ã€‚Mybatis è‡ªåŠ¨å°† java å¯¹è±¡æ˜ å°„è‡³ sql è¯­å¥ã€‚
  * 4ã€å¯¹ç»“æœé›†è§£æéº»çƒ¦ï¼Œsql å˜åŒ–å¯¼è‡´è§£æä»£ç å˜åŒ–ï¼Œä¸”è§£æå‰éœ€è¦éå†ï¼Œå¦‚æœèƒ½å°†æ•°æ®åº“è®°å½•å°è£…æˆ pojo å¯¹è±¡è§£ææ¯”è¾ƒæ–¹ä¾¿ã€‚Mybatis è‡ªåŠ¨å°† sql æ‰§è¡Œç»“æœæ˜ å°„è‡³ java å¯¹è±¡ã€‚

### 2\. Hibernate å’Œ MyBatis æœ‰ä»€ä¹ˆåŒºåˆ«ï¼Ÿ

**ç›¸åŒç‚¹**

  * éƒ½æ˜¯å¯¹ jdbc çš„å°è£…ï¼Œéƒ½æ˜¯åº”ç”¨äºæŒä¹…å±‚çš„æ¡†æ¶ã€‚

![è¿™è¿˜ç”¨è¯´ï¼Ÿ](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-4964e454-7c80-4768-bf0e-d0bf417353ef.gif)è¿™è¿˜ç”¨è¯´ï¼Ÿ

**ä¸åŒç‚¹**

1ï¼‰æ˜ å°„å…³ç³»

  * MyBatis æ˜¯ä¸€ä¸ªåŠè‡ªåŠ¨æ˜ å°„çš„æ¡†æ¶ï¼Œé…ç½® Java å¯¹è±¡ä¸ sql è¯­å¥æ‰§è¡Œç»“æœçš„å¯¹åº”å…³ç³»ï¼Œå¤šè¡¨å…³è”å…³ç³»é…ç½®ç®€å•
  * Hibernate æ˜¯ä¸€ä¸ªå…¨è¡¨æ˜ å°„çš„æ¡†æ¶ï¼Œé…ç½® Java å¯¹è±¡ä¸æ•°æ®åº“è¡¨çš„å¯¹åº”å…³ç³»ï¼Œå¤šè¡¨å…³è”å…³ç³»é…ç½®å¤æ‚

2ï¼‰**SQL ä¼˜åŒ–å’Œç§»æ¤æ€§**

  * Hibernate å¯¹ SQL è¯­å¥å°è£…ï¼Œæä¾›äº†æ—¥å¿—ã€ç¼“å­˜ã€çº§è”ï¼ˆçº§è”æ¯” MyBatis å¼ºå¤§ï¼‰ç­‰ç‰¹æ€§ï¼Œæ­¤å¤–è¿˜æä¾› HQLï¼ˆHibernate Query Languageï¼‰æ“ä½œæ•°æ®åº“ï¼Œæ•°æ®åº“æ— å…³æ€§æ”¯æŒå¥½ï¼Œä½†ä¼šå¤šæ¶ˆè€—æ€§èƒ½ã€‚å¦‚æœé¡¹ç›®éœ€è¦æ”¯æŒå¤šç§æ•°æ®åº“ï¼Œä»£ç å¼€å‘é‡å°‘ï¼Œä½† SQL è¯­å¥ä¼˜åŒ–å›°éš¾ã€‚
  * MyBatis éœ€è¦æ‰‹åŠ¨ç¼–å†™ SQLï¼Œæ”¯æŒåŠ¨æ€ SQLã€å¤„ç†åˆ—è¡¨ã€åŠ¨æ€ç”Ÿæˆè¡¨åã€æ”¯æŒå­˜å‚¨è¿‡ç¨‹ã€‚å¼€å‘å·¥ä½œé‡ç›¸å¯¹å¤§äº›ã€‚ç›´æ¥ä½¿ç”¨ SQL è¯­å¥æ“ä½œæ•°æ®åº“ï¼Œä¸æ”¯æŒæ•°æ®åº“æ— å…³æ€§ï¼Œä½† sql è¯­å¥ä¼˜åŒ–å®¹æ˜“ã€‚

3ï¼‰**MyBatis å’Œ Hibernate çš„é€‚ç”¨åœºæ™¯ä¸åŒ**

![Mybatis vs
Hibernate](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-d1c707f7-0bd0-415c-b190-4757792c072b.png)
Mybatis vs Hibernate

  * Hibernate æ˜¯æ ‡å‡†çš„ ORM æ¡†æ¶ï¼ŒSQL ç¼–å†™é‡è¾ƒå°‘ï¼Œä½†ä¸å¤Ÿçµæ´»ï¼Œé€‚åˆäºéœ€æ±‚ç›¸å¯¹ç¨³å®šï¼Œä¸­å°å‹çš„è½¯ä»¶é¡¹ç›®ï¼Œæ¯”å¦‚ï¼šåŠå…¬è‡ªåŠ¨åŒ–ç³»ç»Ÿ
  * MyBatis æ˜¯åŠ ORM æ¡†æ¶ï¼Œéœ€è¦ç¼–å†™è¾ƒå¤š SQLï¼Œä½†æ˜¯æ¯”è¾ƒçµæ´»ï¼Œé€‚åˆäºéœ€æ±‚å˜åŒ–é¢‘ç¹ï¼Œå¿«é€Ÿè¿­ä»£çš„é¡¹ç›®ï¼Œæ¯”å¦‚ï¼šç”µå•†ç½‘ç«™

### 3\. MyBatis ä½¿ç”¨è¿‡ç¨‹ï¼Ÿç”Ÿå‘½å‘¨æœŸï¼Ÿ

MyBatis åŸºæœ¬ä½¿ç”¨çš„è¿‡ç¨‹å¤§æ¦‚å¯ä»¥åˆ†ä¸ºè¿™ä¹ˆå‡ æ­¥ï¼š

![MybatisåŸºæœ¬ä½¿ç”¨æ­¥éª¤](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-47bab2e8-5c08-4f61-9c0c-dddfe09fb2b5.png)MybatisåŸºæœ¬ä½¿ç”¨æ­¥éª¤

  * 1ï¼‰åˆ›å»º SqlSessionFactory

å¯ä»¥ä»é…ç½®æˆ–è€…ç›´æ¥ç¼–ç æ¥åˆ›å»º SqlSessionFactory

    
    
    String resource = "org/mybatis/example/mybatis-config.xml";
    InputStream inputStream = Resources.getResourceAsStream(resource);
    SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);

  * 2ï¼‰é€šè¿‡ SqlSessionFactory åˆ›å»º SqlSession

SqlSessionï¼ˆä¼šè¯ï¼‰å¯ä»¥ç†è§£ä¸ºç¨‹åºå’Œæ•°æ®åº“ä¹‹é—´çš„æ¡¥æ¢

    
    
    SqlSession session = sqlSessionFactory.openSession();

  * 3ï¼‰é€šè¿‡ sqlsession æ‰§è¡Œæ•°æ®åº“æ“ä½œ

å¯ä»¥é€šè¿‡ SqlSession å®ä¾‹æ¥ç›´æ¥æ‰§è¡Œå·²æ˜ å°„çš„ SQL è¯­å¥ï¼š

    
    
    Blog blog = (Blog)session.selectOne("org.mybatis.example.BlogMapper.selectBlog", 101);

æ›´å¸¸ç”¨çš„æ–¹å¼æ˜¯å…ˆè·å– Mapper(æ˜ å°„)ï¼Œç„¶åå†æ‰§è¡Œ SQL è¯­å¥ï¼š

    
    
    BlogMapper mapper = session.getMapper(BlogMapper.class);
    Blog blog = mapper.selectBlog(101);

  * 4ï¼‰è°ƒç”¨ session.commit()æäº¤äº‹åŠ¡

å¦‚æœæ˜¯æ›´æ–°ã€åˆ é™¤è¯­å¥ï¼Œæˆ‘ä»¬è¿˜éœ€è¦æäº¤ä¸€ä¸‹äº‹åŠ¡ã€‚

  * 5ï¼‰è°ƒç”¨ session.close()å…³é—­ä¼šè¯

æœ€åä¸€å®šè¦è®°å¾—å…³é—­ä¼šè¯ã€‚

#### è¯´è¯´ MyBatis ç”Ÿå‘½å‘¨æœŸï¼Ÿ

ä¸Šé¢æåˆ°äº†å‡ ä¸ª MyBatis çš„ç»„ä»¶ï¼Œä¸€èˆ¬è¯´çš„ MyBatis
ç”Ÿå‘½å‘¨æœŸå°±æ˜¯è¿™äº›ç»„ä»¶çš„ç”Ÿå‘½å‘¨æœŸã€‚

  * SqlSessionFactoryBuilder

ä¸€æ—¦åˆ›å»ºäº† SqlSessionFactoryï¼Œå°±ä¸å†éœ€è¦å®ƒäº†ã€‚ å› æ­¤
SqlSessionFactoryBuilder å®ä¾‹çš„ç”Ÿå‘½å‘¨æœŸåªå­˜åœ¨äºæ–¹æ³•çš„å†…éƒ¨ã€‚

  * SqlSessionFactory

SqlSessionFactory æ˜¯ç”¨æ¥åˆ›å»º SqlSession çš„ï¼Œç›¸å½“äºä¸€ä¸ªæ•°æ®åº“è¿æ¥æ±
ï¼Œæ¯æ¬¡åˆ›å»º SqlSessionFactory
éƒ½ä¼šä½¿ç”¨æ•°æ®åº“èµ„æºï¼Œå¤šæ¬¡åˆ›å»ºå’Œé”€æ¯æ˜¯å¯¹èµ„æºçš„æµªè´¹ã€‚æ‰€ä»¥
SqlSessionFactory æ˜¯åº”ç”¨çº§çš„ç”Ÿå‘½å‘¨æœŸï¼Œè€Œä¸”åº”è¯¥æ˜¯å•ä¾‹çš„ã€‚

  * SqlSession

SqlSession ç›¸å½“äº JDBC ä¸­çš„ Connectionï¼ŒSqlSession
çš„å®ä¾‹ä¸æ˜¯çº¿ç¨‹å®‰å…¨çš„ï¼Œå›
æ­¤æ˜¯ä¸èƒ½è¢«å…±äº«çš„ï¼Œæ‰€ä»¥å®ƒçš„æœ€ä½³çš„ç”Ÿå‘½å‘¨æœŸæ˜¯ä¸€æ¬¡è¯·æ±‚æˆ–ä¸€ä¸ªæ–¹æ³•ã€‚

  * Mapper

æ˜ å°„å™¨æ˜¯ä¸€äº›ç»‘å®šæ˜ å°„è¯­å¥çš„æ¥å£ã€‚æ˜ å°„å™¨æ¥å£çš„å®ä¾‹æ˜¯ä»
SqlSession ä¸­è·å¾—çš„ï¼Œå®ƒçš„ç”Ÿå‘½å‘¨æœŸåœ¨ sqlsession
äº‹åŠ¡æ–¹æ³•ä¹‹å†…ï¼Œä¸€èˆ¬ä¼šæ§åˆ¶åœ¨æ–¹æ³•çº§ã€‚

![MyBatisä¸»è¦ç»„ä»¶ç”Ÿå‘½å‘¨æœŸ](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-79f75371-14c9-4ac9-9d3b-5d80b22705a1.png)MyBatisä¸»è¦ç»„ä»¶ç”Ÿå‘½å‘¨æœŸ

å½“ç„¶ï¼Œä¸‡ç‰©çš†å¯é›†æˆ Springï¼ŒMyBatis é€šå¸¸ä¹Ÿæ˜¯å’Œ Spring
é›†æˆä½¿ç”¨ï¼ŒSpring å¯ä»¥å¸®åŠ©æˆ‘ä»¬åˆ›å»ºçº¿ç¨‹å®‰å…¨çš„ã€åŸºäºäº‹åŠ¡çš„
SqlSession å’Œæ˜ å°„å™¨ï¼Œå¹¶å°†å®ƒä»¬ç›´æ¥æ³¨å…¥åˆ°æˆ‘ä»¬çš„ bean
ä¸­ï¼Œæˆ‘ä»¬ä¸éœ€è¦å…³å¿ƒå®ƒä»¬çš„åˆ›å»ºè¿‡ç¨‹å’Œç”Ÿå‘½å‘¨æœŸï¼Œé‚£å°±æ˜¯å¦å¤–çš„æ•…äº‹äº†ã€‚

![è¿™ä¸ªåº”è¯¥ä¼š](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-2c55dfeb-
bea1-466f-9b1e-d8c001856aa5.png)è¿™ä¸ªåº”è¯¥ä¼š

### 4\. åœ¨ mapper ä¸­å¦‚ä½•ä¼ é€’å¤šä¸ªå‚æ•°ï¼Ÿ

![mapperä¼ é€’å¤šä¸ªå‚æ•°æ–¹æ³•](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-
dd039a20-ae4f-4f6a-b497-01937073198b.png)mapperä¼ é€’å¤šä¸ªå‚æ•°æ–¹æ³•

**æ–¹æ³• 1ï¼šé¡ºåºä¼ å‚æ³•**

    
    
     public User selectUser(String name, int deptId);
    
    <select id="selectUser" resultMap="UserResultMap">
        select * from user
        where user_name = #{0} and dept_id = #{1}
    </select>

  * `\#{}`é‡Œé¢çš„æ•°å­—ä»£è¡¨ä¼ å…¥å‚æ•°çš„é¡ºåºã€‚
  * è¿™ç§æ–¹æ³•ä¸å»ºè®®ä½¿ç”¨ï¼Œsql å±‚è¡¨è¾¾ä¸ç›´è§‚ï¼Œä¸”ä¸€æ—¦é¡ºåºè°ƒæ•´å®¹æ˜“å‡ºé”™ã€‚

**æ–¹æ³• 2ï¼š@Param æ³¨è§£ä¼ å‚æ³•**

    
    
     public User selectUser(@Param("userName") String name, int @Param("deptId") deptId);
    
    <select id="selectUser" resultMap="UserResultMap">
        select * from user
        where user_name = #{userName} and dept_id = #{deptId}
    </select>

  * `\#{}`é‡Œé¢çš„åç§°å¯¹åº”çš„æ˜¯æ³¨è§£@Param æ‹¬å·é‡Œé¢ä¿®é¥°çš„åç§°ã€‚
  * è¿™ç§æ–¹æ³•åœ¨å‚æ•°ä¸å¤šçš„æƒ…å†µè¿˜æ˜¯æ¯”è¾ƒç›´è§‚çš„ï¼Œï¼ˆæ¨èä½¿ç”¨ï¼‰ã€‚

**æ–¹æ³• 3ï¼šMap ä¼ å‚æ³•**

    
    
     public User selectUser(Map<String, Object> params);
    
    <select id="selectUser" parameterType="java.util.Map" resultMap="UserResultMap">
        select * from user
        where user_name = #{userName} and dept_id = #{deptId}
    </select>

  * `\#{}`é‡Œé¢çš„åç§°å¯¹åº”çš„æ˜¯ Map é‡Œé¢çš„ key åç§°ã€‚
  * è¿™ç§æ–¹æ³•é€‚åˆä¼ é€’å¤šä¸ªå‚æ•°ï¼Œä¸”å‚æ•°æ˜“å˜èƒ½çµæ´»ä¼ é€’çš„æƒ…å†µã€‚

**æ–¹æ³• 4ï¼šJava Bean ä¼ å‚æ³•**

    
    
     public User selectUser(User user);
    
    <select id="selectUser" parameterType="com.jourwon.pojo.User" resultMap="UserResultMap">
        select * from user
        where user_name = #{userName} and dept_id = #{deptId}
    </select>

  * `\#{}`é‡Œé¢çš„åç§°å¯¹åº”çš„æ˜¯ User ç±»é‡Œé¢çš„æˆå‘˜å±æ€§ã€‚
  * è¿™ç§æ–¹æ³•ç›´è§‚ï¼Œéœ€è¦å»ºä¸€ä¸ªå®ä½“ç±»ï¼Œæ‰©å±•ä¸å®¹æ˜“ï¼Œéœ€è¦åŠ å±æ€§ï¼Œä½†ä»£ç å¯è¯»æ€§å¼ºï¼Œä¸šåŠ¡é€»è¾‘å¤„ç†æ–¹ä¾¿ï¼Œæ¨èä½¿ç”¨ã€‚ï¼ˆæ¨èä½¿ç”¨ï¼‰ã€‚

### 5\. å®ä½“ç±»å±æ€§åå’Œè¡¨ä¸­å­—æ®µåä¸ä¸€æ · ï¼Œæ€ä¹ˆåŠ?

  * ç¬¬ 1 ç§ï¼š é€šè¿‡åœ¨æŸ¥è¯¢çš„ SQL è¯­å¥ä¸­å®šä¹‰å­—æ®µåçš„åˆ«åï¼Œè®©å­—æ®µåçš„åˆ«åå’Œå®ä½“ç±»çš„å±æ€§åä¸€è‡´ã€‚

    
    
    <select id="getOrder" parameterType="int" resultType="com.jourwon.pojo.Order">
           select order_id id, order_no orderno ,order_price price form orders where order_id=#{id};
    </select>

  * ç¬¬ 2 ç§ï¼š é€šè¿‡ resultMap ä¸­çš„<result>æ¥æ˜ å°„å­—æ®µåå’Œå®ä½“ç±»å±æ€§åçš„ä¸€ä¸€å¯¹åº”çš„å…³ç³»ã€‚

    
    
    <select id="getOrder" parameterType="int" resultMap="orderResultMap">
      select * from orders where order_id=#{id}
    </select>
    
    <resultMap type="com.jourwon.pojo.Order" id="orderResultMap">
        <!â€“ç”¨idå±æ€§æ¥æ˜ å°„ä¸»é”®å­—æ®µâ€“>
        <id property="id" column="order_id">
        <!â€“ç”¨resultå±æ€§æ¥æ˜ å°„éä¸»é”®å­—æ®µï¼Œpropertyä¸ºå®ä½“ç±»å±æ€§åï¼Œcolumnä¸ºæ•°æ®åº“è¡¨ä¸­çš„å±æ€§â€“>
      <result property ="orderno" column ="order_no"/>
      <result property="price" column="order_price" />
    </resultMap>

### 6\. Mybatis æ˜¯å¦å¯ä»¥æ˜ å°„ Enum æšä¸¾ç±»ï¼Ÿ

  * Mybatis å½“ç„¶å¯ä»¥æ˜ å°„æšä¸¾ç±»ï¼Œä¸å•å¯ä»¥æ˜ å°„æšä¸¾ç±»ï¼ŒMybatis å¯ä»¥æ˜ å°„ä»»ä½•å¯¹è±¡åˆ°è¡¨çš„ä¸€åˆ—ä¸Šã€‚æ˜ å°„æ–¹å¼ä¸ºè‡ªå®šä¹‰ä¸€ä¸ª TypeHandlerï¼Œå®ç° TypeHandler çš„ setParameter()å’Œ getResult()æ¥å£æ–¹æ³•ã€‚
  * TypeHandler æœ‰ä¸¤ä¸ªä½œç”¨ï¼Œä¸€æ˜¯å®Œæˆä» javaType è‡³ jdbcType çš„è½¬æ¢ï¼ŒäºŒæ˜¯å®Œæˆ jdbcType è‡³ javaType çš„è½¬æ¢ï¼Œä½“ç°ä¸º setParameter()å’Œ getResult()ä¸¤ä¸ªæ–¹æ³•ï¼Œåˆ†åˆ«ä»£è¡¨è®¾ç½® sql é—®å·å ä½ç¬¦å‚æ•°å’Œè·å–åˆ—æŸ¥è¯¢ç»“æœã€‚

### 7\. #{}å’Œ${}çš„åŒºåˆ«?

`#{}` æ˜¯é¢„ç¼–è¯‘å¤„ç†ï¼Œ`${}` æ˜¯å­—ç¬¦ä¸²æ›¿æ¢ã€‚

â‘ ã€å½“ä½¿ç”¨ `#{}` æ—¶ï¼ŒMyBatis ä¼šåœ¨ SQL æ‰§è¡Œä¹‹å‰ï¼Œå°†å
ä½ç¬¦æ›¿æ¢ä¸ºé—®å· `?`ï¼Œå¹¶ä½¿ç”¨å‚æ•°å€¼æ¥æ›¿ä»£è¿™äº›é—®å·ã€‚

ç”±äº `#{}` ä½¿ç”¨äº†é¢„å¤„ç†ï¼Œæ‰€ä»¥èƒ½æœ‰æ•ˆé˜²æ­¢ SQL
æ³¨å…¥ï¼Œç¡®ä¿å‚æ•°å€¼åœ¨åˆ°è¾¾æ•°æ®åº“ä¹‹å‰è¢«æ­£ç¡®åœ°å¤„ç†å’Œè½¬ä¹‰ã€‚

    
    
    <select id="selectUser" resultType="User">
      SELECT * FROM users WHERE id = #{id}
    </select>

â‘¡ã€å½“ä½¿ç”¨ `${}` æ—¶ï¼Œå‚æ•°çš„å€¼ä¼šç›´æ¥æ›¿æ¢åˆ° SQL
è¯­å¥ä¸­å»ï¼Œè€Œä¸ä¼šç»è¿‡é¢„å¤„ç†ã€‚

è¿™å°±å­˜åœ¨ SQL æ³¨å…¥çš„é£é™©ï¼Œå› ä¸ºå‚æ•°å€¼ä¼šç›´æ¥æ‹¼æ¥åˆ° SQL
è¯­å¥ä¸­ï¼Œå‡å¦‚å‚æ•°å€¼æ˜¯ `1 or 1=1`ï¼Œé‚£ä¹ˆ SQL è¯­å¥å°±ä¼šå˜æˆ `SELECT *
FROM users WHERE id = 1 or 1=1`ï¼Œè¿™æ
·å°±ä¼šå¯¼è‡´æŸ¥è¯¢å‡ºæ‰€æœ‰ç”¨æˆ·çš„ç»“æœã€‚

`${}`
é€šå¸¸ç”¨äºé‚£äº›ä¸èƒ½ä½¿ç”¨é¢„å¤„ç†çš„åœºåˆï¼Œæ¯”å¦‚è¯´åŠ¨æ€è¡¨åã€åˆ—åã€æ’åºç­‰ï¼Œè¦æå‰å¯¹å‚æ•°è¿›è¡Œå®‰å…¨æ€§æ
¡éªŒã€‚

    
    
    <select id="selectUsersByOrder" resultType="User">
      SELECT * FROM users ORDER BY ${columnName} ASC
    </select>

>   1. [Java
> é¢è¯•æŒ‡å—ï¼ˆä»˜è´¹ï¼‰](https://javabetter.cn/zhishixingqiu/mianshi.html)æ”¶å½•çš„å°å…¬å¸é¢ç»åˆé›†åŒå­¦
> 1 Java åç«¯é¢è¯•åŸé¢˜ï¼šMybatis#()å’Œ$()æœ‰ä»€ä¹ˆåŒºåˆ«?
>   2. [Java
> é¢è¯•æŒ‡å—ï¼ˆä»˜è´¹ï¼‰](https://javabetter.cn/zhishixingqiu/mianshi.html)æ”¶å½•çš„äº¬ä¸œé¢ç»åŒå­¦
> 5 Java åç«¯æŠ€æœ¯ä¸€é¢é¢è¯•åŸé¢˜ï¼š#{}å’Œ${}çš„åŒºåˆ«
>

### 8\. æ¨¡ç³ŠæŸ¥è¯¢ like è¯­å¥è¯¥æ€ä¹ˆå†™?

![concatæ‹¼æ¥like](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-e5dde8ba-7808-410b-986a-2fc15ba55e21.png)concatæ‹¼æ¥like

  * 1 â€™`%${question}%`â€™ å¯èƒ½å¼•èµ· SQL æ³¨å…¥ï¼Œä¸æ¨è
  * 2 `"%"#{question}"%"` æ³¨æ„ï¼šå› ä¸º`#{â€¦}`è§£ææˆ sql è¯­å¥æ—¶å€™ï¼Œä¼šåœ¨å˜é‡å¤–ä¾§è‡ªåŠ¨åŠ å•å¼•å·â€™ 'ï¼Œæ‰€ä»¥è¿™é‡Œ % éœ€è¦ä½¿ç”¨åŒå¼•å·" "ï¼Œä¸èƒ½ä½¿ç”¨å•å¼•å· â€™ 'ï¼Œä¸ç„¶ä¼šæŸ¥ä¸åˆ°ä»»ä½•ç»“æœã€‚
  * 3 `CONCAT('%',#{question},'%')` ä½¿ç”¨ CONCAT()å‡½æ•°ï¼Œï¼ˆæ¨è âœ¨ï¼‰
  * 4 ä½¿ç”¨ bind æ ‡ç­¾ï¼ˆä¸æ¨èï¼‰

    
    
    <select id="listUserLikeUsername" resultType="com.jourwon.pojo.User">
    &emsp;&emsp;<bind name="pattern" value="'%' + username + '%'" />
    &emsp;&emsp;select id,sex,age,username,password from person where username LIKE #{pattern}
    </select>

### 9\. Mybatis èƒ½æ‰§è¡Œä¸€å¯¹ä¸€ã€ä¸€å¯¹å¤šçš„å…³è”æŸ¥è¯¢å—ï¼Ÿ

å½“ç„¶å¯ä»¥ï¼Œä¸æ­¢æ”¯æŒä¸€å¯¹ä¸€ã€ä¸€å¯¹å¤šçš„å…³è”æŸ¥è¯¢ï¼Œè¿˜æ”¯æŒå¤šå¯¹å¤šã€å¤šå¯¹ä¸€çš„å…³è”æŸ¥è¯¢ã€‚

![MyBatisçº§è”](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-
aa1e0cc1-1a5f-4efe-9aed-3081b15c9a2a.png)MyBatisçº§è”

  * **ä¸€å¯¹ä¸€ <association>**

æ¯”å¦‚è®¢å•å’Œæ”¯ä»˜æ˜¯ä¸€å¯¹ä¸€çš„å…³ç³»ï¼Œè¿™ç§å…³è”çš„å®ç°ï¼š

å®ä½“ç±»:

    
    
    public class Order {
        private Integer orderId;
        private String orderDesc;
    
        /**
         * æ”¯ä»˜å¯¹è±¡
         */
        private Pay pay;
        //â€¦â€¦
    }

ç»“æœæ˜ å°„

    
    
    <!-- è®¢å•resultMap -->
    <resultMap id="peopleResultMap" type="cn.fighter3.entity.Order">
        <id property="orderId" column="order_id" />
        <result property="orderDesc" column="order_desc"/>
        <!--ä¸€å¯¹ä¸€ç»“æœæ˜ å°„-->
        <association property="pay" javaType="cn.fighter3.entity.Pay">
            <id column="payId" property="pay_id"/>
            <result column="account" property="account"/>
        </association>
    </resultMap>

æŸ¥è¯¢å°±æ˜¯æ™®é€šçš„å…³è”æŸ¥

    
    
    <select id="getTeacher" resultMap="getTeacherMap" parameterType="int">
        select * from order o
         left join pay p on o.order_id=p.order_id
        where  o.order_id=#{orderId}
    </select>

  * **ä¸€å¯¹å¤š`<collection>`**

æ¯”å¦‚å•†å“åˆ†ç±»å’Œå•†å“ï¼Œæ˜¯ä¸€å¯¹å¤šçš„å…³ç³»ã€‚

  * å®ä½“ç±»

    
    
    public class Category {
        private int categoryId;
        private String categoryName;
    
        /**
        * å•†å“åˆ—è¡¨
        **/
        List<Product> products;
        //â€¦â€¦
    }

  * ç»“æœæ˜ å°„

    
    
    <resultMap type="Category" id="categoryBean">
        <id column="categoryId" property="category_id" />
        <result column="categoryName" property="category_name" />
    
        <!-- ä¸€å¯¹å¤šçš„å…³ç³» -->
        <!-- property: æŒ‡çš„æ˜¯é›†åˆå±æ€§çš„å€¼, ofTypeï¼šæŒ‡çš„æ˜¯é›†åˆä¸­å…ƒç´ çš„ç±»å‹ -->
        <collection property="products" ofType="Product">
            <id column="product_id" property="productId" />
            <result column="productName" property="productName" />
            <result column="price" property="price" />
        </collection>
    </resultMap>

  * æŸ¥è¯¢

æŸ¥è¯¢å°±æ˜¯ä¸€ä¸ªæ™®é€šçš„å…³è”æŸ¥è¯¢

    
    
    <!-- å…³è”æŸ¥è¯¢åˆ†ç±»å’Œäº§å“è¡¨ -->
    <select id="listCategory" resultMap="categoryBean">
        select c.*, p.* from category_ c left join product_ p on c.id = p.cid
    </select>

â€‹
é‚£ä¹ˆå¤šå¯¹ä¸€ã€å¤šå¯¹å¤šæ€ä¹ˆå®ç°å‘¢ï¼Ÿè¿˜æ˜¯åˆ©ç”¨<association>å’Œ<collection>ï¼Œç¯‡å¹…æ‰€é™ï¼Œè¿™é‡Œå°±ä¸å±•å¼€äº†ã€‚

### 10\. Mybatis æ˜¯å¦æ”¯æŒå»¶è¿ŸåŠ è½½ï¼ŸåŸç†ï¼Ÿ

  * Mybatis æ”¯æŒ association å…³è”å¯¹è±¡å’Œ collection å…³è”é›†åˆå¯¹è±¡çš„å»¶è¿ŸåŠ è½½ï¼Œassociation æŒ‡çš„å°±æ˜¯ä¸€å¯¹ä¸€ï¼Œcollection æŒ‡çš„å°±æ˜¯ä¸€å¯¹å¤šæŸ¥è¯¢ã€‚åœ¨ Mybatis é…ç½®æ–‡ä»¶ä¸­ï¼Œå¯ä»¥é…ç½®æ˜¯å¦å¯ç”¨å»¶è¿ŸåŠ è½½ lazyLoadingEnabled=true|falseã€‚
  * å®ƒçš„åŸç†æ˜¯ï¼Œä½¿ç”¨ CGLIB åˆ›å»ºç›®æ ‡å¯¹è±¡çš„ä»£ç†å¯¹è±¡ï¼Œå½“è°ƒç”¨ç›®æ ‡æ–¹æ³•æ—¶ï¼Œè¿›å…¥æ‹¦æˆªå™¨æ–¹æ³•ï¼Œæ¯”å¦‚è°ƒç”¨ a.getB().getName()ï¼Œæ‹¦æˆªå™¨ invoke()æ–¹æ³•å‘ç° a.getB()æ˜¯ null å€¼ï¼Œé‚£ä¹ˆå°±ä¼šå•ç‹¬å‘é€äº‹å…ˆä¿å­˜å¥½çš„æŸ¥è¯¢å…³è” B å¯¹è±¡çš„ sqlï¼ŒæŠŠ B æŸ¥è¯¢ä¸Šæ¥ï¼Œç„¶åè°ƒç”¨ a.setB(b)ï¼Œäºæ˜¯ a çš„å¯¹è±¡ b å±æ€§å°±æœ‰å€¼äº†ï¼Œæ¥ç€å®Œæˆ a.getB().getName()æ–¹æ³•çš„è°ƒç”¨ã€‚è¿™å°±æ˜¯å»¶è¿ŸåŠ è½½çš„åŸºæœ¬åŸç†ã€‚
  * å½“ç„¶äº†ï¼Œä¸å…‰æ˜¯ Mybatisï¼Œå‡ ä¹æ‰€æœ‰çš„åŒ…æ‹¬ Hibernateï¼Œæ”¯æŒå»¶è¿ŸåŠ è½½çš„åŸç†éƒ½æ˜¯ä¸€æ ·çš„ã€‚

### 11\. å¦‚ä½•è·å–ç”Ÿæˆçš„ä¸»é”®?

  * æ–°å¢æ ‡ç­¾ä¸­æ·»åŠ ï¼škeyProperty=" ID " å³å¯

    
    
    <insert id="insert" useGeneratedKeys="true" keyProperty="userId" >
        insert into user(
        user_name, user_password, create_time)
        values(#{userName}, #{userPassword} , #{createTime, jdbcType= TIMESTAMP})
    </insert>

  * è¿™æ—¶å€™å°±å¯ä»¥å®Œæˆå›å¡«ä¸»é”®

    
    
    mapper.insert(user);
    user.getId;

### 12\. MyBatis æ”¯æŒåŠ¨æ€ SQL å—ï¼Ÿ

MyBatis ä¸­æœ‰ä¸€äº›æ”¯æŒåŠ¨æ€ SQL çš„æ ‡ç­¾ï¼Œå®ƒä»¬çš„åŸç†æ˜¯ä½¿ç”¨ OGNL ä»
SQL å‚æ•°å¯¹è±¡ä¸­è®¡ç®—è¡¨è¾¾å¼çš„å€¼ï¼Œæ ¹æ®è¡¨è¾¾å¼çš„å€¼åŠ¨æ€æ‹¼æ¥
SQLï¼Œä»¥æ­¤æ¥å®ŒæˆåŠ¨æ€ SQL çš„åŠŸèƒ½ã€‚

![MyBatis](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-f52c027d-25a5-4bd9-b5d3-1421655546a5.png)MyBatis

  * if

æ ¹æ®æ¡ä»¶æ¥ç»„æˆ where å­å¥

    
    
    <select id="findActiveBlogWithTitleLike"
       resultType="Blog">
    SELECT * FROM BLOG
    WHERE state = â€˜ACTIVEâ€™
    <if test="title != null">
      AND title like #{title}
    </if>
    </select>

  * choose (when, otherwise)

è¿™ä¸ªå’Œ Java ä¸­çš„ switch è¯­å¥æœ‰ç‚¹åƒ

    
    
    <select id="findActiveBlogLike"
       resultType="Blog">
    SELECT * FROM BLOG WHERE state = â€˜ACTIVEâ€™
    <choose>
      <when test="title != null">
        AND title like #{title}
      </when>
      <when test="author != null and author.name != null">
        AND author_name like #{author.name}
      </when>
      <otherwise>
        AND featured = 1
      </otherwise>
    </choose>
    </select>

  * trim (where, set)

  * <where>å¯ä»¥ç”¨åœ¨æ‰€æœ‰çš„æŸ¥è¯¢æ¡ä»¶éƒ½æ˜¯åŠ¨æ€çš„æƒ…å†µ

    
    
    <select id="findActiveBlogLike"
       resultType="Blog">
    SELECT * FROM BLOG
    <where>
      <if test="state != null">
           state = #{state}
      </if>
      <if test="title != null">
          AND title like #{title}
      </if>
      <if test="author != null and author.name != null">
          AND author_name like #{author.name}
      </if>
    </where>
    </select>

  * <set> å¯ä»¥ç”¨åœ¨åŠ¨æ€æ›´æ–°çš„æ—¶å€™

    
    
    <update id="updateAuthorIfNecessary">
      update Author
        <set>
          <if test="username != null">username=#{username},</if>
          <if test="password != null">password=#{password},</if>
          <if test="email != null">email=#{email},</if>
          <if test="bio != null">bio=#{bio}</if>
        </set>
      where id=#{id}
    </update>

  * foreach

çœ‹åˆ°åå­—å°±çŸ¥é“äº†ï¼Œè¿™ä¸ªæ˜¯ç”¨æ¥å¾ªç¯çš„ï¼Œå¯ä»¥å¯¹é›†åˆè¿›è¡Œéå†

    
    
    <select id="selectPostIn" resultType="domain.blog.Post">
    SELECT *
    FROM POST P
    <where>
      <foreach item="item" index="index" collection="list"
          open="ID in (" separator="," close=")" nullable="true">
            #{item}
      </foreach>
    </where>
    </select>

### 13\. MyBatis å¦‚ä½•æ‰§è¡Œæ‰¹é‡æ“ä½œï¼Ÿ

![MyBatisæ‰¹é‡æ“ä½œ](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-24225f07-fbe6-40c8-a63b-a94983f9107a.png)MyBatisæ‰¹é‡æ“ä½œ

**ç¬¬ä¸€ç§æ–¹æ³•ï¼šä½¿ç”¨ foreach æ ‡ç­¾**

foreach çš„ä¸»è¦ç”¨åœ¨æ„å»º in æ¡ä»¶ä¸­ï¼Œå®ƒå¯ä»¥åœ¨ SQL
è¯­å¥ä¸­è¿›è¡Œè¿­ä»£ä¸€ä¸ªé›†åˆã€‚foreach æ ‡ç­¾çš„å±æ€§ä¸»è¦æœ‰
itemï¼Œindexï¼Œcollectionï¼Œopenï¼Œseparatorï¼Œcloseã€‚

  * itemâ€ƒâ€ƒ è¡¨ç¤ºé›†åˆä¸­æ¯ä¸€ä¸ªå…ƒç´ è¿›è¡Œè¿­ä»£æ—¶çš„åˆ«åï¼Œéšä¾¿èµ·çš„å˜é‡åï¼›
  * indexâ€ƒâ€ƒ æŒ‡å®šä¸€ä¸ªåå­—ï¼Œç”¨äºè¡¨ç¤ºåœ¨è¿­ä»£è¿‡ç¨‹ä¸­ï¼Œæ¯æ¬¡è¿­ä»£åˆ°çš„ä½ç½®ï¼Œä¸å¸¸ç”¨ï¼›
  * openâ€ƒâ€ƒ è¡¨ç¤ºè¯¥è¯­å¥ä»¥ä»€ä¹ˆå¼€å§‹ï¼Œå¸¸ç”¨â€œ(â€ï¼›
  * separator è¡¨ç¤ºåœ¨æ¯æ¬¡è¿›è¡Œè¿­ä»£ä¹‹é—´ä»¥ä»€ä¹ˆç¬¦å·ä½œä¸ºåˆ†éš”ç¬¦ï¼Œå¸¸ç”¨â€œ,â€ï¼›
  * closeâ€ƒâ€ƒ è¡¨ç¤ºä»¥ä»€ä¹ˆç»“æŸï¼Œå¸¸ç”¨â€œ)â€ã€‚

åœ¨ä½¿ç”¨ foreach çš„æ—¶å€™æœ€å…³é”®çš„ä¹Ÿæ˜¯æœ€å®¹æ˜“å‡ºé”™çš„å°±æ˜¯
collection
å±æ€§ï¼Œè¯¥å±æ€§æ˜¯å¿…é¡»æŒ‡å®šçš„ï¼Œä½†æ˜¯åœ¨ä¸åŒæƒ…å†µä¸‹ï¼Œè¯¥å±æ€§çš„å€¼æ˜¯ä¸ä¸€æ
·çš„ï¼Œä¸»è¦æœ‰ä»¥ä¸‹ 3 ç§æƒ…å†µï¼š

  1. å¦‚æœä¼ å…¥çš„æ˜¯å•å‚æ•°ä¸”å‚æ•°ç±»å‹æ˜¯ä¸€ä¸ª List çš„æ—¶å€™ï¼Œcollection å±æ€§å€¼ä¸º list
  2. å¦‚æœä¼ å…¥çš„æ˜¯å•å‚æ•°ä¸”å‚æ•°ç±»å‹æ˜¯ä¸€ä¸ª array æ•°ç»„çš„æ—¶å€™ï¼Œcollection çš„å±æ€§å€¼ä¸º array
  3. å¦‚æœä¼ å…¥çš„å‚æ•°æ˜¯å¤šä¸ªçš„æ—¶å€™ï¼Œæˆ‘ä»¬å°±éœ€è¦æŠŠå®ƒä»¬å°è£…æˆä¸€ä¸ª Map äº†ï¼Œå½“ç„¶å•å‚æ•°ä¹Ÿå¯ä»¥å°è£…æˆ mapï¼Œå®é™…ä¸Šå¦‚æœä½ åœ¨ä¼ å…¥å‚æ•°çš„æ—¶å€™ï¼Œåœ¨ MyBatis é‡Œé¢ä¹Ÿæ˜¯ä¼šæŠŠå®ƒå°è£…æˆä¸€ä¸ª Map çš„ï¼Œmap çš„ key å°±æ˜¯å‚æ•°åï¼Œæ‰€ä»¥è¿™ä¸ªæ—¶å€™ collection å±æ€§å€¼å°±æ˜¯ä¼ å…¥çš„ List æˆ– array å¯¹è±¡åœ¨è‡ªå·±å°è£…çš„ map é‡Œé¢çš„ key

çœ‹çœ‹æ‰¹é‡ä¿å­˜çš„ä¸¤ç§ç”¨æ³•ï¼š

    
    
    <!-- MySQLä¸‹æ‰¹é‡ä¿å­˜ï¼Œå¯ä»¥foreachéå† mysqlæ”¯æŒvalues(),(),()è¯­æ³• --> //æ¨èä½¿ç”¨
    <insert id="addEmpsBatch">
        INSERT INTO emp(ename,gender,email,did)
        VALUES
        <foreach collection="emps" item="emp" separator=",">
            (#{emp.eName},#{emp.gender},#{emp.email},#{emp.dept.id})
        </foreach>
    </insert>
    
    
    <!-- è¿™ç§æ–¹å¼éœ€è¦æ•°æ®åº“è¿æ¥å±æ€§allowMutiQueries=trueçš„æ”¯æŒ
     å¦‚jdbc.url=jdbc:mysql://localhost:3306/mybatis?allowMultiQueries=true -->
    <insert id="addEmpsBatch">
        <foreach collection="emps" item="emp" separator=";">
            INSERT INTO emp(ename,gender,email,did)
            VALUES(#{emp.eName},#{emp.gender},#{emp.email},#{emp.dept.id})
        </foreach>
    </insert>

**ç¬¬äºŒç§æ–¹æ³•ï¼šä½¿ç”¨ ExecutorType.BATCH**

  * Mybatis å†…ç½®çš„ ExecutorType æœ‰ 3 ç§ï¼Œé»˜è®¤ä¸º simpleï¼Œè¯¥æ¨¡å¼ä¸‹å®ƒä¸ºæ¯ä¸ªè¯­å¥çš„æ‰§è¡Œåˆ›å»ºä¸€ä¸ªæ–°çš„é¢„å¤„ç†è¯­å¥ï¼Œå•æ¡æäº¤ sqlï¼›è€Œ batch æ¨¡å¼é‡å¤ä½¿ç”¨å·²ç»é¢„å¤„ç†çš„è¯­å¥ï¼Œå¹¶ä¸”æ‰¹é‡æ‰§è¡Œæ‰€æœ‰æ›´æ–°è¯­å¥ï¼Œæ˜¾ç„¶ batch æ€§èƒ½å°†æ›´ä¼˜ï¼› ä½† batch æ¨¡å¼ä¹Ÿæœ‰è‡ªå·±çš„é—®é¢˜ï¼Œæ¯”å¦‚åœ¨ Insert æ“ä½œæ—¶ï¼Œåœ¨äº‹åŠ¡æ²¡æœ‰æäº¤ä¹‹å‰ï¼Œæ˜¯æ²¡æœ‰åŠæ³•è·å–åˆ°è‡ªå¢çš„ idï¼Œåœ¨æŸäº›æƒ…å†µä¸‹ä¸ç¬¦åˆä¸šåŠ¡çš„éœ€æ±‚ã€‚

å…·ä½“ç”¨æ³•å¦‚ä¸‹ï¼š

    
    
    //æ‰¹é‡ä¿å­˜æ–¹æ³•æµ‹è¯•
    @Test
    public void testBatch() throws IOException{
        SqlSessionFactory sqlSessionFactory = getSqlSessionFactory();
        //å¯ä»¥æ‰§è¡Œæ‰¹é‡æ“ä½œçš„sqlSession
        SqlSession openSession = sqlSessionFactory.openSession(ExecutorType.BATCH);
    
        //æ‰¹é‡ä¿å­˜æ‰§è¡Œå‰æ—¶é—´
        long start = System.currentTimeMillis();
        try {
            EmployeeMapper mapper = openSession.getMapper(EmployeeMapper.class);
            for (int i = 0; i < 1000; i++) {
                mapper.addEmp(new Employee(UUID.randomUUID().toString().substring(0, 5), "b", "1"));
            }
    
            openSession.commit();
            long end = System.currentTimeMillis();
            //æ‰¹é‡ä¿å­˜æ‰§è¡Œåçš„æ—¶é—´
            System.out.println("æ‰§è¡Œæ—¶é•¿" + (end - start));
            //æ‰¹é‡ é¢„ç¼–è¯‘sqlä¸€æ¬¡==ã€‹è®¾ç½®å‚æ•°==ã€‹10000æ¬¡==ã€‹æ‰§è¡Œ1æ¬¡   677
            //éæ‰¹é‡  ï¼ˆé¢„ç¼–è¯‘=è®¾ç½®å‚æ•°=æ‰§è¡Œ ï¼‰==ã€‹10000æ¬¡   1121
    
        } finally {
            openSession.close();
        }
    }

  * mapper å’Œ mapper.xml å¦‚ä¸‹

    
    
    public interface EmployeeMapper {
        //æ‰¹é‡ä¿å­˜å‘˜å·¥
        Long addEmp(Employee employee);
    }
    
    
    <mapper namespace="com.jourwon.mapper.EmployeeMapper"
         <!--æ‰¹é‡ä¿å­˜å‘˜å·¥ -->
        <insert id="addEmp">
            insert into employee(lastName,email,gender)
            values(#{lastName},#{email},#{gender})
        </insert>
    </mapper>

### 14\. è¯´è¯´ Mybatis çš„ä¸€çº§ã€äºŒçº§ç¼“å­˜ï¼Ÿ

  1. ä¸€çº§ç¼“å­˜: åŸºäº PerpetualCache çš„ HashMap æœ¬åœ°ç¼“å­˜ï¼Œå…¶å­˜å‚¨ä½œç”¨åŸŸä¸º SqlSessionï¼Œå„ä¸ª SqlSession ä¹‹é—´çš„ç¼“å­˜ç›¸äº’éš”ç¦»ï¼Œå½“ Session flush æˆ– close ä¹‹åï¼Œè¯¥ SqlSession ä¸­çš„æ‰€æœ‰ Cache å°±å°†æ¸…ç©ºï¼ŒMyBatis é»˜è®¤æ‰“å¼€ä¸€çº§ç¼“å­˜ã€‚

![Mybatisä¸€çº§ç¼“å­˜](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-54afb458-7dfc-4d48-9a90-4ad1a8739937.png)Mybatisä¸€çº§ç¼“å­˜

  2. äºŒçº§ç¼“å­˜ä¸ä¸€çº§ç¼“å­˜å…¶æœºåˆ¶ç›¸åŒï¼Œé»˜è®¤ä¹Ÿæ˜¯é‡‡ç”¨ PerpetualCacheï¼ŒHashMap å­˜å‚¨ï¼Œä¸åŒä¹‹å¤„åœ¨äºå…¶å­˜å‚¨ä½œç”¨åŸŸä¸º Mapper(Namespace)ï¼Œå¯ä»¥åœ¨å¤šä¸ª SqlSession ä¹‹é—´å…±äº«ï¼Œå¹¶ä¸”å¯è‡ªå®šä¹‰å­˜å‚¨æºï¼Œå¦‚ Ehcacheã€‚é»˜è®¤ä¸æ‰“å¼€äºŒçº§ç¼“å­˜ï¼Œè¦å¼€å¯äºŒçº§ç¼“å­˜ï¼Œä½¿ç”¨äºŒçº§ç¼“å­˜å±æ€§ç±»éœ€è¦å®ç° Serializable åºåˆ—åŒ–æ¥å£(å¯ç”¨æ¥ä¿å­˜å¯¹è±¡çš„çŠ¶æ€),å¯åœ¨å®ƒçš„æ˜ å°„æ–‡ä»¶ä¸­é…ç½®ã€‚

![MybatisäºŒçº§ç¼“å­˜ç¤ºæ„å›¾](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-8dae71da-
ffd4-43f5-9ee9-258ea82d216b.png)MybatisäºŒçº§ç¼“å­˜ç¤ºæ„å›¾

GitHub ä¸Šæ ‡æ˜Ÿ 10000+ çš„å¼€æºçŸ¥è¯†åº“ã€Š[äºŒå“¥çš„ Java
è¿›é˜¶ä¹‹è·¯](https://github.com/itwanger/toBeBetterJavaer)ã€‹ç¬¬ä¸€ç‰ˆ PDF
ç»ˆäºæ¥äº†ï¼åŒ…æ‹¬ Java åŸºç¡€è¯­æ³•ã€æ•°ç»„&å­—ç¬¦ä¸²ã€OOPã€é›†åˆæ¡†æ¶ã€Java
IOã€å¼‚å¸¸å¤„ç†ã€Java æ–°ç‰¹æ€§ã€ç½‘ç»œç¼–ç¨‹ã€NIOã€å¹¶å‘ç¼–ç¨‹ã€JVM
ç­‰ç­‰ï¼Œå…±è®¡ 32 ä¸‡ä½™å­—ï¼Œ500+å¼
æ‰‹ç»˜å›¾ï¼Œå¯ä»¥è¯´æ˜¯é€šä¿—æ˜“æ‡‚ã€é£è¶£å¹½é»˜â€¦â€¦è¯¦æƒ…æˆ³ï¼š[å¤ªèµäº†ï¼ŒGitHub
ä¸Šæ ‡æ˜Ÿ 10000+ çš„ Java æ•™ç¨‹](https://javabetter.cn/overview/)

å¾®ä¿¡æœ **æ²‰é»˜ç‹äºŒ** æˆ–æ‰«æä¸‹æ–¹äºŒç»´ç
å…³æ³¨äºŒå“¥çš„åŸåˆ›å…¬ä¼—å·æ²‰é»˜ç‹äºŒï¼Œå›å¤ **222** å³å¯å…è´¹é¢†å–ã€‚

![](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/gongzhonghao.png)

## åŸç†

### 15\. èƒ½è¯´è¯´ MyBatis çš„å·¥ä½œåŸç†å—ï¼Ÿ

æˆ‘ä»¬å·²ç»å¤§æ¦‚çŸ¥é“äº† MyBatis
çš„å·¥ä½œæµç¨‹ï¼ŒæŒ‰å·¥ä½œåŸç†ï¼Œå¯ä»¥åˆ†ä¸ºä¸¤å¤§æ­¥ï¼š`ç”Ÿæˆä¼šè¯å·¥å‚`ã€`ä¼šè¯è¿è¡Œ`ã€‚

![MyBatisçš„å·¥ä½œæµç¨‹](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-61ac17ef-9eee-48c0-9a2d-545e1d554b13.png)MyBatisçš„å·¥ä½œæµç¨‹

MyBatis
æ˜¯ä¸€ä¸ªæˆç†Ÿçš„æ¡†æ¶ï¼Œç¯‡å¹…é™åˆ¶ï¼Œè¿™é‡ŒæŠ“å¤§æ”¾å°ï¼Œæ¥çœ‹çœ‹å®ƒçš„ä¸»è¦å·¥ä½œæµç¨‹ã€‚

> **æ„å»ºä¼šè¯å·¥å‚**

æ„é€ ä¼šè¯å·¥å‚ä¹Ÿå¯ä»¥åˆ†ä¸ºä¸¤æ­¥ï¼š

![æ„å»ºä¼šè¯å·¥å‚](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-234a4d1b-2d44-4576-9954-26f56162750e.png)æ„å»ºä¼šè¯å·¥å‚

  * è·å–é…ç½®

è·å–é…ç½®è¿™ä¸€æ­¥ç»è¿‡äº†å‡ æ­¥è½¬åŒ–ï¼Œæœ€ç»ˆç”±ç”Ÿæˆäº†ä¸€ä¸ªé…ç½®ç±»
Configuration å®ä¾‹ï¼Œè¿™ä¸ªé…ç½®ç±»å®ä¾‹éå¸¸é‡è¦ï¼Œä¸»è¦ä½œç”¨åŒ…æ‹¬ï¼š

  * è¯»å–é…ç½®æ–‡ä»¶ï¼ŒåŒ…æ‹¬åŸºç¡€é…ç½®æ–‡ä»¶å’Œæ˜ å°„æ–‡ä»¶
  * åˆå§‹åŒ–åŸºç¡€é…ç½®ï¼Œæ¯”å¦‚ MyBatis çš„åˆ«åï¼Œè¿˜æœ‰å…¶å®ƒçš„ä¸€äº›é‡è¦çš„ç±»å¯¹è±¡ï¼Œåƒæ’ä»¶ã€æ˜ å°„å™¨ã€ObjectFactory ç­‰ç­‰
  * æä¾›ä¸€ä¸ªå•ä¾‹ï¼Œä½œä¸ºä¼šè¯å·¥å‚æ„å»ºçš„é‡è¦å‚æ•°
  * å®ƒçš„æ„å»ºè¿‡ç¨‹ä¹Ÿä¼šåˆå§‹åŒ–ä¸€äº›ç¯å¢ƒå˜é‡ï¼Œæ¯”å¦‚æ•°æ®æº

    
    
    public SqlSessionFactory build(Reader reader, String environment, Properties properties) {
          SqlSessionFactory var5;
          //çœç•¥å¼‚å¸¸å¤„ç†
              //xmlé…ç½®æ„å»ºå™¨
              XMLConfigBuilder parser = new XMLConfigBuilder(reader, environment, properties);
              //é€šè¿‡è½¬åŒ–çš„Configurationæ„å»ºSqlSessionFactory
              var5 = this.build(parser.parse());
    }

  * æ„å»º SqlSessionFactory

SqlSessionFactory
åªæ˜¯ä¸€ä¸ªæ¥å£ï¼Œæ„å»ºå‡ºæ¥çš„å®é™…ä¸Šæ˜¯å®ƒçš„å®ç°ç±»çš„å®ä¾‹ï¼Œä¸€èˆ¬æˆ‘ä»¬ç”¨çš„éƒ½æ˜¯å®ƒçš„å®ç°ç±»
DefaultSqlSessionFactoryï¼Œ

    
    
    public SqlSessionFactory build(Configuration config) {
        return new DefaultSqlSessionFactory(config);
    }

> **ä¼šè¯è¿è¡Œ**

ä¼šè¯è¿è¡Œæ˜¯ MyBatis
æœ€å¤æ‚çš„éƒ¨åˆ†ï¼Œå®ƒçš„è¿è¡Œç¦»ä¸å¼€å››å¤§ç»„ä»¶çš„é…åˆï¼š

![MyBatisä¼šè¯è¿è¡Œå››å¤§å…³é”®ç»„ä»¶](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-
da477d50-209e-45b3-a003-6d63e674bd99.png)MyBatisä¼šè¯è¿è¡Œå››å¤§å…³é”®ç»„ä»¶

  * Executorï¼ˆæ‰§è¡Œå™¨ï¼‰

Executor èµ·åˆ°äº†è‡³å…³é‡è¦çš„ä½œç”¨ï¼ŒSqlSession
åªæ˜¯ä¸€ä¸ªé—¨é¢ï¼Œç›¸å½“äºå®¢æœï¼ŒçœŸæ­£å¹²æ´»çš„æ˜¯æ˜¯
Executorï¼Œå°±åƒæ˜¯é»˜é»˜æ—
é—»çš„å·¥ç¨‹å¸ˆã€‚å®ƒæä¾›äº†ç›¸åº”çš„æŸ¥è¯¢å’Œæ›´æ–°æ–¹æ³•ï¼Œä»¥åŠäº‹åŠ¡æ–¹æ³•ã€‚

    
    
    Environment environment = this.configuration.getEnvironment();
    TransactionFactory transactionFactory = this.getTransactionFactoryFromEnvironment(environment);
    tx = transactionFactory.newTransaction(environment.getDataSource(), level, autoCommit);
    //é€šè¿‡Configurationåˆ›å»ºexecutor
    Executor executor = this.configuration.newExecutor(tx, execType);
    var8 = new DefaultSqlSession(this.configuration, executor, autoCommit);

  * StatementHandlerï¼ˆæ•°æ®åº“ä¼šè¯å™¨ï¼‰

StatementHandlerï¼Œé¡¾åæ€ä¹‰ï¼Œå¤„ç†æ•°æ®åº“ä¼šè¯çš„ã€‚æˆ‘ä»¬ä»¥
SimpleExecutor ä¸ºä¾‹ï¼Œçœ‹ä¸€ä¸‹å®ƒçš„æŸ¥è¯¢æ–¹æ³•ï¼Œå…ˆç”Ÿæˆäº†ä¸€ä¸ª
StatementHandler å®ä¾‹ï¼Œå†æ‹¿è¿™ä¸ª handler å»æ‰§è¡Œ queryã€‚

    
    
     public <E> List<E> doQuery(MappedStatement ms, Object parameter, RowBounds rowBounds, ResultHandler resultHandler, BoundSql boundSql) throws SQLException {
        Statement stmt = null;
    
        List var9;
        try {
            Configuration configuration = ms.getConfiguration();
            StatementHandler handler = configuration.newStatementHandler(this.wrapper, ms, parameter, rowBounds, resultHandler, boundSql);
            stmt = this.prepareStatement(handler, ms.getStatementLog());
            var9 = handler.query(stmt, resultHandler);
        } finally {
            this.closeStatement(stmt);
        }
    
        return var9;
    }

å†ä»¥æœ€å¸¸ç”¨çš„ PreparedStatementHandler çœ‹ä¸€ä¸‹å®ƒçš„ query
æ–¹æ³•ï¼Œå…¶å®åœ¨ä¸Šé¢çš„`prepareStatement`å·²ç»å¯¹å‚æ•°è¿›è¡Œäº†é¢„ç¼–è¯‘å¤„ç†ï¼Œåˆ°äº†è¿™é‡Œï¼Œå°±ç›´æ¥æ‰§è¡Œ
sqlï¼Œä½¿ç”¨ ResultHandler å¤„ç†è¿”å›ç»“æœã€‚

    
    
    public <E> List<E> query(Statement statement, ResultHandler resultHandler) throws SQLException {
        PreparedStatement ps = (PreparedStatement)statement;
        ps.execute();
        return this.resultSetHandler.handleResultSets(ps);
    }

  * ParameterHandler ï¼ˆå‚æ•°å¤„ç†å™¨ï¼‰

PreparedStatementHandler é‡Œå¯¹ sql è¿›è¡Œäº†é¢„ç¼–è¯‘å¤„ç†

    
    
    public void parameterize(Statement statement) throws SQLException {
        this.parameterHandler.setParameters((PreparedStatement)statement);
    }

è¿™é‡Œç”¨çš„å°±æ˜¯ ParameterHandlerï¼ŒsetParameters
çš„ä½œç”¨å°±æ˜¯è®¾ç½®é¢„ç¼–è¯‘ SQL è¯­å¥çš„å‚æ•°ã€‚

é‡Œé¢è¿˜ä¼šç”¨åˆ° typeHandler ç±»å‹å¤„ç†å™¨ï¼Œå¯¹ç±»å‹è¿›è¡Œå¤„ç†ã€‚

    
    
    public interface ParameterHandler {
        Object getParameterObject();
    
        void setParameters(PreparedStatement var1) throws SQLException;
    }

  * ResultSetHandlerï¼ˆç»“æœå¤„ç†å™¨ï¼‰

æˆ‘ä»¬å‰é¢ä¹Ÿçœ‹åˆ°äº†ï¼Œæœ€åçš„ç»“æœè¦é€šè¿‡ ResultSetHandler
æ¥è¿›è¡Œå¤„ç†ï¼ŒhandleResultSets
è¿™ä¸ªæ–¹æ³•å°±æ˜¯ç”¨æ¥åŒ…è£…ç»“æœé›†çš„ã€‚Mybatis ä¸ºæˆ‘ä»¬æä¾›äº†ä¸€ä¸ª
DefaultResultSetHandlerï¼Œé€šå¸¸éƒ½æ˜¯ç”¨è¿™ä¸ªå®ç°ç±»å»è¿›è¡Œç»“æœçš„å¤„ç†çš„ã€‚

    
    
    public interface ResultSetHandler {
      <E> List<E> handleResultSets(Statement var1) throws SQLException;
    
      <E> Cursor<E> handleCursorResultSets(Statement var1) throws SQLException;
    
      void handleOutputParameters(CallableStatement var1) throws SQLException;
    }

å®ƒä¼šä½¿ç”¨ typeHandle å¤„ç†ç±»å‹ï¼Œç„¶åç”¨ ObjectFactory
æä¾›çš„è§„åˆ™ç»„è£…å¯¹è±¡ï¼Œè¿”å›ç»™è°ƒç”¨è€…ã€‚

æ•´ä½“ä¸Šæ€»ç»“ä¸€ä¸‹ä¼šè¯è¿è¡Œï¼š

![ä¼šè¯è¿è¡Œçš„ç®€å•ç¤ºæ„å›¾](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-
ebd0712a-1f62-4154-b391-2cb596634710.png)ä¼šè¯è¿è¡Œçš„ç®€å•ç¤ºæ„å›¾

> æˆ‘ä»¬æœ€åæŠŠæ•´ä¸ªçš„å·¥ä½œæµç¨‹ä¸²è”èµ·æ¥ï¼Œç®€å•æ€»ç»“ä¸€ä¸‹ï¼š

![MyBatisæ•´ä½“å·¥ä½œåŸç†å›¾](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-
dc142e94-8e7f-4ec6-a1f6-1d20669292ad.png)MyBatisæ•´ä½“å·¥ä½œåŸç†å›¾

  1. è¯»å– MyBatis é…ç½®æ–‡ä»¶â€”â€”mybatis-config.xml ã€åŠ è½½æ˜ å°„æ–‡ä»¶â€”â€”æ˜ å°„æ–‡ä»¶å³ SQL æ˜ å°„æ–‡ä»¶ï¼Œæ–‡ä»¶ä¸­é…ç½®äº†æ“ä½œæ•°æ®åº“çš„ SQL è¯­å¥ã€‚æœ€åç”Ÿæˆä¸€ä¸ªé…ç½®å¯¹è±¡ã€‚
  2. æ„é€ ä¼šè¯å·¥å‚ï¼šé€šè¿‡ MyBatis çš„ç¯å¢ƒç­‰é…ç½®ä¿¡æ¯æ„å»ºä¼šè¯å·¥å‚ SqlSessionFactoryã€‚
  3. åˆ›å»ºä¼šè¯å¯¹è±¡ï¼šç”±ä¼šè¯å·¥å‚åˆ›å»º SqlSession å¯¹è±¡ï¼Œè¯¥å¯¹è±¡ä¸­åŒ…å«äº†æ‰§è¡Œ SQL è¯­å¥çš„æ‰€æœ‰æ–¹æ³•ã€‚
  4. Executor æ‰§è¡Œå™¨ï¼šMyBatis åº•å±‚å®šä¹‰äº†ä¸€ä¸ª Executor æ¥å£æ¥æ“ä½œæ•°æ®åº“ï¼Œå®ƒå°†æ ¹æ® SqlSession ä¼ é€’çš„å‚æ•°åŠ¨æ€åœ°ç”Ÿæˆéœ€è¦æ‰§è¡Œçš„ SQL è¯­å¥ï¼ŒåŒæ—¶è´Ÿè´£æŸ¥è¯¢ç¼“å­˜çš„ç»´æŠ¤ã€‚
  5. StatementHandlerï¼šæ•°æ®åº“ä¼šè¯å™¨ï¼Œä¸²è”èµ·å‚æ•°æ˜ å°„çš„å¤„ç†å’Œè¿è¡Œç»“æœæ˜ å°„çš„å¤„ç†ã€‚
  6. å‚æ•°å¤„ç†ï¼šå¯¹è¾“å…¥å‚æ•°çš„ç±»å‹è¿›è¡Œå¤„ç†ï¼Œå¹¶é¢„ç¼–è¯‘ã€‚
  7. ç»“æœå¤„ç†ï¼šå¯¹è¿”å›ç»“æœçš„ç±»å‹è¿›è¡Œå¤„ç†ï¼Œæ ¹æ®å¯¹è±¡æ˜ å°„è§„åˆ™ï¼Œè¿”å›ç›¸åº”çš„å¯¹è±¡ã€‚

### 16\. MyBatis çš„åŠŸèƒ½æ¶æ„æ˜¯ä»€ä¹ˆæ ·çš„ï¼Ÿ

![MyBatisåŠŸèƒ½æ¶æ„](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-c7b59a67-49f4-48f8-a25d-033daeea7e3e.png)MyBatisåŠŸèƒ½æ¶æ„

æˆ‘ä»¬ä¸€èˆ¬æŠŠ Mybatis çš„åŠŸèƒ½æ¶æ„åˆ†ä¸ºä¸‰å±‚ï¼š

  * API æ¥å£å±‚ï¼šæä¾›ç»™å¤–éƒ¨ä½¿ç”¨çš„æ¥å£ APIï¼Œå¼€å‘äººå‘˜é€šè¿‡è¿™äº›æœ¬åœ° API æ¥æ“çºµæ•°æ®åº“ã€‚æ¥å£å±‚ä¸€æ¥æ”¶åˆ°è°ƒç”¨è¯·æ±‚å°±ä¼šè°ƒç”¨æ•°æ®å¤„ç†å±‚æ¥å®Œæˆå…·ä½“çš„æ•°æ®å¤„ç†ã€‚
  * æ•°æ®å¤„ç†å±‚ï¼šè´Ÿè´£å…·ä½“çš„ SQL æŸ¥æ‰¾ã€SQL è§£æã€SQL æ‰§è¡Œå’Œæ‰§è¡Œç»“æœæ˜ å°„å¤„ç†ç­‰ã€‚å®ƒä¸»è¦çš„ç›®çš„æ˜¯æ ¹æ®è°ƒç”¨çš„è¯·æ±‚å®Œæˆä¸€æ¬¡æ•°æ®åº“æ“ä½œã€‚
  * åŸºç¡€æ”¯æ’‘å±‚ï¼šè´Ÿè´£æœ€åŸºç¡€çš„åŠŸèƒ½æ”¯æ’‘ï¼ŒåŒ…æ‹¬è¿æ¥ç®¡ç†ã€äº‹åŠ¡ç®¡ç†ã€é…ç½®åŠ è½½å’Œç¼“å­˜å¤„ç†ï¼Œè¿™äº›éƒ½æ˜¯å…±ç”¨çš„ä¸œè¥¿ï¼Œå°†ä»–ä»¬æŠ½å–å‡ºæ¥ä½œä¸ºæœ€åŸºç¡€çš„ç»„ä»¶ã€‚ä¸ºä¸Šå±‚çš„æ•°æ®å¤„ç†å±‚æä¾›æœ€åŸºç¡€çš„æ”¯æ’‘ã€‚

### 17\. ä¸ºä»€ä¹ˆ Mapper æ¥å£ä¸éœ€è¦å®ç°ç±»ï¼Ÿ

å››ä¸ªå­—å›ç­”ï¼š**åŠ¨æ€ä»£ç†** ï¼Œæˆ‘ä»¬æ¥çœ‹ä¸€ä¸‹è·å– Mapper çš„è¿‡ç¨‹ï¼š

![Mapperä»£ç†](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-15e30a15-f34c-4aa4-b131-4ddc8620348e.png)Mapperä»£ç†

  * è·å– Mapper

æˆ‘ä»¬éƒ½çŸ¥é“å®šä¹‰çš„ Mapper æ¥å£æ˜¯æ²¡æœ‰å®ç°ç±»çš„ï¼ŒMapper æ˜
å°„å…¶å®æ˜¯é€šè¿‡**åŠ¨æ€ä»£ç†** å®ç°çš„ã€‚

    
    
    BlogMapper mapper = session.getMapper(BlogMapper.class);

ä¸ƒæ‹å…«ç»•åœ°è¿›å»çœ‹ä¸€ä¸‹ï¼Œå‘ç°è·å– Mapper çš„è¿‡ç¨‹ï¼Œéœ€è¦å…ˆè·å–
MapperProxyFactoryâ€”â€”Mapper ä»£ç†å·¥å‚ã€‚

    
    
    public <T> T getMapper(Class<T> type, SqlSession sqlSession) {
        MapperProxyFactory<T> mapperProxyFactory = (MapperProxyFactory)this.knownMappers.get(type);
        if (mapperProxyFactory == null) {
            throw new BindingException("Type " + type + " is not known to the MapperRegistry.");
        } else {
            try {
                return mapperProxyFactory.newInstance(sqlSession);
            } catch (Exception var5) {
                throw new BindingException("Error getting mapper instance. Cause: " + var5, var5);
            }
        }
    }

  * MapperProxyFactory

MapperProxyFactory çš„ä½œç”¨æ˜¯ç”Ÿæˆ MapperProxyï¼ˆMapper ä»£ç†å¯¹è±¡ï¼‰ã€‚

    
    
    public class MapperProxyFactory<T> {
      private final Class<T> mapperInterface;
      â€¦â€¦
      protected T newInstance(MapperProxy<T> mapperProxy) {
          return Proxy.newProxyInstance(this.mapperInterface.getClassLoader(), new Class[]{this.mapperInterface}, mapperProxy);
      }
    
      public T newInstance(SqlSession sqlSession) {
          MapperProxy<T> mapperProxy = new MapperProxy(sqlSession, this.mapperInterface, this.methodCache);
          return this.newInstance(mapperProxy);
      }
    }

è¿™é‡Œå¯ä»¥çœ‹åˆ°åŠ¨æ€ä»£ç†å¯¹æ¥å£çš„ç»‘å®šï¼Œå®ƒçš„ä½œç”¨å°±æ˜¯ç”ŸæˆåŠ¨æ€ä»£ç†å¯¹è±¡ï¼ˆå
ä½ï¼‰ï¼Œè€Œä»£ç†çš„æ–¹æ³•è¢«æ”¾åˆ°äº† MapperProxy ä¸­ã€‚

  * MapperProxy

MapperProxy é‡Œï¼Œé€šå¸¸ä¼šç”Ÿæˆä¸€ä¸ª MapperMethod å¯¹è±¡ï¼Œå®ƒæ˜¯é€šè¿‡
cachedMapperMethod æ–¹æ³•å¯¹å…¶è¿›è¡Œåˆå§‹åŒ–çš„ï¼Œç„¶åæ‰§è¡Œ excute æ–¹æ³•ã€‚

    
    
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        try {
            return Object.class.equals(method.getDeclaringClass()) ? method.invoke(this, args) : this.cachedInvoker(method).invoke(proxy, method, args, this.sqlSession);
        } catch (Throwable var5) {
            throw ExceptionUtil.unwrapThrowable(var5);
        }
    }

  * MapperMethod

MapperMethod é‡Œçš„ excute æ–¹æ³•ï¼Œä¼šçœŸæ­£å»æ‰§è¡Œ
sqlã€‚è¿™é‡Œç”¨åˆ°äº†å‘½ä»¤æ¨¡å¼ï¼Œå…¶å®ç»•ä¸€åœˆï¼Œæœ€ç»ˆå®ƒè¿˜æ˜¯é€šè¿‡
SqlSession çš„å®ä¾‹å»è¿è¡Œå¯¹è±¡çš„ sqlã€‚

    
    
    public Object execute(SqlSession sqlSession, Object[] args) {
          Object result;
          Object param;
          â€¦â€¦
          case SELECT:
              if (this.method.returnsVoid() && this.method.hasResultHandler()) {
                  this.executeWithResultHandler(sqlSession, args);
                  result = null;
              } else if (this.method.returnsMany()) {
                  result = this.executeForMany(sqlSession, args);
              } else if (this.method.returnsMap()) {
                  result = this.executeForMap(sqlSession, args);
              } else if (this.method.returnsCursor()) {
                  result = this.executeForCursor(sqlSession, args);
              } else {
                  param = this.method.convertArgsToSqlCommandParam(args);
                  result = sqlSession.selectOne(this.command.getName(), param);
                  if (this.method.returnsOptional() && (result == null || !this.method.getReturnType().equals(result.getClass()))) {
                      result = Optional.ofNullable(result);
                  }
              }
              break;
             â€¦â€¦
      }

### 18.Mybatis éƒ½æœ‰å“ªäº› Executor æ‰§è¡Œå™¨ï¼Ÿ

![Mybatis
Executorç±»å‹](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-59340143-5155-4719-869e-304b5738b2f2.png)Mybatis
Executorç±»å‹

Mybatis æœ‰ä¸‰ç§åŸºæœ¬çš„ Executor
æ‰§è¡Œå™¨ï¼ŒSimpleExecutorã€ReuseExecutorã€BatchExecutorã€‚

  * **SimpleExecutor** ï¼šæ¯æ‰§è¡Œä¸€æ¬¡ update æˆ– selectï¼Œå°±å¼€å¯ä¸€ä¸ª Statement å¯¹è±¡ï¼Œç”¨å®Œç«‹åˆ»å…³é—­ Statement å¯¹è±¡ã€‚
  * **ReuseExecutor** ï¼šæ‰§è¡Œ update æˆ– selectï¼Œä»¥ sql ä½œä¸º key æŸ¥æ‰¾ Statement å¯¹è±¡ï¼Œå­˜åœ¨å°±ä½¿ç”¨ï¼Œä¸å­˜åœ¨å°±åˆ›å»ºï¼Œç”¨å®Œåï¼Œä¸å…³é—­ Statement å¯¹è±¡ï¼Œè€Œæ˜¯æ”¾ç½®äº Map<String, Statement>å†…ï¼Œä¾›ä¸‹ä¸€æ¬¡ä½¿ç”¨ã€‚ç®€è¨€ä¹‹ï¼Œå°±æ˜¯é‡å¤ä½¿ç”¨ Statement å¯¹è±¡ã€‚
  * **BatchExecutor** ï¼šæ‰§è¡Œ updateï¼ˆæ²¡æœ‰ selectï¼ŒJDBC æ‰¹å¤„ç†ä¸æ”¯æŒ selectï¼‰ï¼Œå°†æ‰€æœ‰ sql éƒ½æ·»åŠ åˆ°æ‰¹å¤„ç†ä¸­ï¼ˆaddBatch()ï¼‰ï¼Œç­‰å¾…ç»Ÿä¸€æ‰§è¡Œï¼ˆexecuteBatch()ï¼‰ï¼Œå®ƒç¼“å­˜äº†å¤šä¸ª Statement å¯¹è±¡ï¼Œæ¯ä¸ª Statement å¯¹è±¡éƒ½æ˜¯ addBatch()å®Œæ¯•åï¼Œç­‰å¾…é€ä¸€æ‰§è¡Œ executeBatch()æ‰¹å¤„ç†ã€‚ä¸ JDBC æ‰¹å¤„ç†ç›¸åŒã€‚

ä½œç”¨èŒƒå›´ï¼šExecutor çš„è¿™äº›ç‰¹ç‚¹ï¼Œéƒ½ä¸¥æ ¼é™åˆ¶åœ¨ SqlSession
ç”Ÿå‘½å‘¨æœŸèŒƒå›´å†…ã€‚

> **Mybatis ä¸­å¦‚ä½•æŒ‡å®šä½¿ç”¨å“ªä¸€ç§ Executor æ‰§è¡Œå™¨ï¼Ÿ**

  * åœ¨ Mybatis é…ç½®æ–‡ä»¶ä¸­ï¼Œåœ¨è®¾ç½®ï¼ˆsettingsï¼‰å¯ä»¥æŒ‡å®šé»˜è®¤çš„ ExecutorType æ‰§è¡Œå™¨ç±»å‹ï¼Œä¹Ÿå¯ä»¥æ‰‹åŠ¨ç»™ DefaultSqlSessionFactory çš„åˆ›å»º SqlSession çš„æ–¹æ³•ä¼ é€’ ExecutorType ç±»å‹å‚æ•°ï¼Œå¦‚`SqlSession openSession(ExecutorType execType)`ã€‚
  * é…ç½®é»˜è®¤çš„æ‰§è¡Œå™¨ã€‚SIMPLE å°±æ˜¯æ™®é€šçš„æ‰§è¡Œå™¨ï¼›REUSE æ‰§è¡Œå™¨ä¼šé‡ç”¨é¢„å¤„ç†è¯­å¥ï¼ˆprepared statementsï¼‰ï¼› BATCH æ‰§è¡Œå™¨å°†é‡ç”¨è¯­å¥å¹¶æ‰§è¡Œæ‰¹é‡æ›´æ–°ã€‚

GitHub ä¸Šæ ‡æ˜Ÿ 10000+ çš„å¼€æºçŸ¥è¯†åº“ã€Š[äºŒå“¥çš„ Java
è¿›é˜¶ä¹‹è·¯](https://github.com/itwanger/toBeBetterJavaer)ã€‹ç¬¬ä¸€ç‰ˆ PDF
ç»ˆäºæ¥äº†ï¼åŒ…æ‹¬ Java åŸºç¡€è¯­æ³•ã€æ•°ç»„&å­—ç¬¦ä¸²ã€OOPã€é›†åˆæ¡†æ¶ã€Java
IOã€å¼‚å¸¸å¤„ç†ã€Java æ–°ç‰¹æ€§ã€ç½‘ç»œç¼–ç¨‹ã€NIOã€å¹¶å‘ç¼–ç¨‹ã€JVM
ç­‰ç­‰ï¼Œå…±è®¡ 32 ä¸‡ä½™å­—ï¼Œ500+å¼
æ‰‹ç»˜å›¾ï¼Œå¯ä»¥è¯´æ˜¯é€šä¿—æ˜“æ‡‚ã€é£è¶£å¹½é»˜â€¦â€¦è¯¦æƒ…æˆ³ï¼š[å¤ªèµäº†ï¼ŒGitHub
ä¸Šæ ‡æ˜Ÿ 10000+ çš„ Java æ•™ç¨‹](https://javabetter.cn/overview/)

å¾®ä¿¡æœ **æ²‰é»˜ç‹äºŒ** æˆ–æ‰«æä¸‹æ–¹äºŒç»´ç
å…³æ³¨äºŒå“¥çš„åŸåˆ›å…¬ä¼—å·æ²‰é»˜ç‹äºŒï¼Œå›å¤ **222** å³å¯å…è´¹é¢†å–ã€‚

![](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/gongzhonghao.png)

## æ’ä»¶

### 19\. è¯´è¯´ Mybatis çš„æ’ä»¶è¿è¡ŒåŸç†ï¼Œå¦‚ä½•ç¼–å†™ä¸€ä¸ªæ’ä»¶ï¼Ÿ

> **æ’ä»¶çš„è¿è¡ŒåŸç†ï¼Ÿ**

Mybatis ä¼šè¯çš„è¿è¡Œéœ€è¦
ParameterHandlerã€ResultSetHandlerã€StatementHandlerã€Executor
è¿™å››å¤§å¯¹è±¡çš„é…åˆï¼Œæ’ä»¶çš„åŸç†å°±æ˜¯åœ¨è¿™å››å¤§å¯¹è±¡è°ƒåº¦çš„æ—¶å€™ï¼Œæ’å…¥ä¸€äº›æˆ‘æˆ‘ä»¬è‡ªå·±çš„ä»£ç
ã€‚

![MyBatisæ’ä»¶åŸç†ç®€å›¾](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-00f2581b-5aae-441a-83f7-75641b3ba010.png)MyBatisæ’ä»¶åŸç†ç®€å›¾

Mybatis ä½¿ç”¨ JDK çš„åŠ¨æ€ä»£ç†ï¼Œä¸ºç›®æ
‡å¯¹è±¡ç”Ÿæˆä»£ç†å¯¹è±¡ã€‚å®ƒæä¾›äº†ä¸€ä¸ªå·¥å…·ç±»`Plugin`ï¼Œå®ç°äº†`InvocationHandler`æ¥å£ã€‚

![Pluginä¸­è°ƒç”¨æ’ä»¶æ–¹æ³•](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-c487f77a-9b87-4d9b-9a49-5aa87401b5e8.png)Pluginä¸­è°ƒç”¨æ’ä»¶æ–¹æ³•

ä½¿ç”¨`Plugin`ç”Ÿæˆä»£ç†å¯¹è±¡ï¼Œä»£ç†å¯¹è±¡åœ¨è°ƒç”¨æ–¹æ³•çš„æ—¶å€™ï¼Œå°±ä¼šè¿›å…¥
invoke æ–¹æ³•ï¼Œåœ¨ invoke
æ–¹æ³•ä¸­ï¼Œå¦‚æœå­˜åœ¨ç­¾åçš„æ‹¦æˆªæ–¹æ³•ï¼Œæ’ä»¶çš„ intercept
æ–¹æ³•å°±ä¼šåœ¨è¿™é‡Œè¢«æˆ‘ä»¬è°ƒç”¨ï¼Œç„¶åå°±è¿”å›ç»“æœã€‚å¦‚æœä¸å­˜åœ¨ç­¾åæ–¹æ³•ï¼Œé‚£ä¹ˆå°†ç›´æ¥åå°„è°ƒç”¨æˆ‘ä»¬è¦æ‰§è¡Œçš„æ–¹æ³•ã€‚

> **å¦‚ä½•ç¼–å†™ä¸€ä¸ªæ’ä»¶ï¼Ÿ**

æˆ‘ä»¬è‡ªå·±ç¼–å†™ MyBatis æ’ä»¶ï¼Œåªéœ€è¦å®ç°æ‹¦æˆªå™¨æ¥å£ `Interceptor
(org.apache.ibatis. plugin Interceptor
ï¼‰`ï¼Œåœ¨å®ç°ç±»ä¸­å¯¹æ‹¦æˆªå¯¹è±¡å’Œæ–¹æ³•è¿›è¡Œå¤„ç†ã€‚

  * å®ç° Mybatis çš„ Interceptor æ¥å£å¹¶é‡å†™ intercept()æ–¹æ³•

è¿™é‡Œæˆ‘ä»¬åªæ˜¯åœ¨ç›®æ ‡å¯¹è±¡æ‰§è¡Œç›®æ ‡æ–¹æ³•çš„å‰åè¿›è¡Œäº†æ‰“å°ï¼›

    
    
    public class MyInterceptor implements Interceptor {
        Properties props=null;
    
        @Override
        public Object intercept(Invocation invocation) throws Throwable {
            System.out.println("beforeâ€¦â€¦");
            //å¦‚æœå½“å‰ä»£ç†çš„æ˜¯ä¸€ä¸ªéä»£ç†å¯¹è±¡ï¼Œé‚£ä¹ˆå°±ä¼šè°ƒç”¨çœŸå®æ‹¦æˆªå¯¹è±¡çš„æ–¹æ³•
            // å¦‚æœä¸æ˜¯å®ƒå°±ä¼šè°ƒç”¨ä¸‹ä¸ªæ’ä»¶ä»£ç†å¯¹è±¡çš„invokeæ–¹æ³•
            Object obj=invocation.proceed();
            System.out.println("afterâ€¦â€¦");
            return obj;
        }
    }

  * ç„¶åå†ç»™æ’ä»¶ç¼–å†™æ³¨è§£ï¼Œç¡®å®šè¦æ‹¦æˆªçš„å¯¹è±¡ï¼Œè¦æ‹¦æˆªçš„æ–¹æ³•

    
    
    @Intercepts({@Signature(
            type = Executor.class,  //ç¡®å®šè¦æ‹¦æˆªçš„å¯¹è±¡
            method = "update",        //ç¡®å®šè¦æ‹¦æˆªçš„æ–¹æ³•
            args = {MappedStatement.class,Object.class}   //æ‹¦æˆªæ–¹æ³•çš„å‚æ•°
    )})
    public class MyInterceptor implements Interceptor {
        Properties props=null;
    
        @Override
        public Object intercept(Invocation invocation) throws Throwable {
            System.out.println("beforeâ€¦â€¦");
            //å¦‚æœå½“å‰ä»£ç†çš„æ˜¯ä¸€ä¸ªéä»£ç†å¯¹è±¡ï¼Œé‚£ä¹ˆå°±ä¼šè°ƒç”¨çœŸå®æ‹¦æˆªå¯¹è±¡çš„æ–¹æ³•
            // å¦‚æœä¸æ˜¯å®ƒå°±ä¼šè°ƒç”¨ä¸‹ä¸ªæ’ä»¶ä»£ç†å¯¹è±¡çš„invokeæ–¹æ³•
            Object obj=invocation.proceed();
            System.out.println("afterâ€¦â€¦");
            return obj;
        }
    }

  * æœ€åï¼Œå† MyBatis é…ç½®æ–‡ä»¶é‡Œé¢é…ç½®æ’ä»¶

    
    
    <plugins>
        <plugin interceptor="xxx.MyPlugin">
           <property name="dbType",value="mysql"/>
        </plugin>
    </plugins>

### 20\. MyBatis æ˜¯å¦‚ä½•è¿›è¡Œåˆ†é¡µçš„ï¼Ÿåˆ†é¡µæ’ä»¶çš„åŸç†æ˜¯ä»€ä¹ˆï¼Ÿ

> **MyBatis æ˜¯å¦‚ä½•åˆ†é¡µçš„ï¼Ÿ**

MyBatis ä½¿ç”¨ RowBounds å¯¹è±¡è¿›è¡Œåˆ†é¡µï¼Œå®ƒæ˜¯é’ˆå¯¹ ResultSet
ç»“æœé›†æ‰§è¡Œçš„å†…å­˜åˆ†é¡µï¼Œè€Œéç‰©ç†åˆ†é¡µã€‚å¯ä»¥åœ¨ sql
å†…ç›´æ¥ä¹¦å†™å¸¦æœ‰ç‰©ç†åˆ†é¡µçš„å‚æ•°æ¥å®Œæˆç‰©ç†åˆ†é¡µåŠŸèƒ½ï¼Œä¹Ÿå¯ä»¥ä½¿ç”¨åˆ†é¡µæ’ä»¶æ¥å®Œæˆç‰©ç†åˆ†é¡µã€‚

> **åˆ†é¡µæ’ä»¶çš„åŸç†æ˜¯ä»€ä¹ˆï¼Ÿ**

  * åˆ†é¡µæ’ä»¶çš„åŸºæœ¬åŸç†æ˜¯ä½¿ç”¨ Mybatis æä¾›çš„æ’ä»¶æ¥å£ï¼Œå®ç°è‡ªå®šä¹‰æ’ä»¶ï¼Œæ‹¦æˆª Executor çš„ query æ–¹æ³•
  * åœ¨æ‰§è¡ŒæŸ¥è¯¢çš„æ—¶å€™ï¼Œæ‹¦æˆªå¾…æ‰§è¡Œçš„ sqlï¼Œç„¶åé‡å†™ sqlï¼Œæ ¹æ® dialect æ–¹è¨€ï¼Œæ·»åŠ å¯¹åº”çš„ç‰©ç†åˆ†é¡µè¯­å¥å’Œç‰©ç†åˆ†é¡µå‚æ•°ã€‚
  * ä¸¾ä¾‹ï¼š`select * from student`ï¼Œæ‹¦æˆª sql åé‡å†™ä¸ºï¼š`select t.* from (select * from student) t limit 0, 10`

å¯ä»¥çœ‹ä¸€ä¸‹ä¸€ä¸ªå¤§æ¦‚çš„ MyBatis é€šç”¨åˆ†é¡µæ‹¦æˆªå™¨ï¼š

![Mybatis-é€šç”¨åˆ†é¡µæ‹¦æˆªå™¨](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/sidebar/sanfene/mybatis-0bcdca85-e127-44ff-92e0-368a3f089ec8.png)Mybatis-é€šç”¨åˆ†é¡µæ‹¦æˆªå™¨

## è¡¥å……

### 21.è¯´è¯´ JDBC çš„æ‰§è¡Œæ­¥éª¤ï¼Ÿ

> 2024 å¹´ 03 æœˆ 19 æ—¥å¢è¡¥

Java æ•°æ®åº“è¿æ¥ï¼ˆJDBCï¼‰æ˜¯ä¸€ä¸ªç”¨äºæ‰§è¡Œ SQL è¯­å¥çš„ Java
APIï¼Œå®ƒä¸ºå¤šç§å…³ç³»æ•°æ®åº“æä¾›äº†ç»Ÿä¸€è®¿é—®çš„æœºåˆ¶ã€‚ä½¿ç”¨ JDBC
æ“ä½œæ•°æ®åº“é€šå¸¸æ¶‰åŠä»¥ä¸‹æ­¥éª¤ï¼š

ç¬¬ä¸€æ­¥ï¼ŒåŠ è½½æ•°æ®åº“é©±åŠ¨

åœ¨ä¸æ•°æ®åº“å»ºç«‹è¿æ¥ä¹‹å‰ï¼Œé¦–å…ˆéœ€è¦é€šè¿‡`Class.forName()`æ–¹æ³•åŠ
è½½å¯¹åº”çš„æ•°æ®åº“é©±åŠ¨ã€‚è¿™ä¸€æ­¥ç¡®ä¿ JDBC
é©±åŠ¨æ³¨å†Œåˆ°äº†`DriverManager`ç±»ä¸­ã€‚

    
    
    Class.forName("com.mysql.cj.jdbc.Driver");

ç¬¬äºŒæ­¥ï¼Œå»ºç«‹æ•°æ®åº“è¿æ¥

ä½¿ç”¨`DriverManager.getConnection()`æ–¹æ³•å»ºç«‹åˆ°æ•°æ®åº“çš„è¿æ¥ã€‚è¿™ä¸€æ­¥éœ€è¦æä¾›æ•°æ®åº“
URLã€ç”¨æˆ·åå’Œå¯†ç ä½œä¸ºå‚æ•°ã€‚

    
    
    Connection conn = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/databaseName", "username", "password");

ç¬¬ä¸‰æ­¥ï¼Œåˆ›å»º`Statement`å¯¹è±¡

é€šè¿‡å»ºç«‹çš„æ•°æ®åº“è¿æ¥å¯¹è±¡`Connection`åˆ›å»º`Statement`ã€`PreparedStatement`æˆ–`CallableStatement`å¯¹è±¡ï¼Œç”¨äºæ‰§è¡Œ
SQL è¯­å¥ã€‚

    
    
    Statement stmt = conn.createStatement();

æˆ–è€…åˆ›å»º`PreparedStatement`å¯¹è±¡ï¼ˆé¢„ç¼–è¯‘ SQL
è¯­å¥ï¼Œé€‚ç”¨äºå¸¦å‚æ•°çš„ SQLï¼‰ï¼š

    
    
    PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM tableName WHERE column = ?");
    pstmt.setString(1, "value");

ç¬¬å››æ­¥ï¼Œæ‰§è¡Œ SQL è¯­å¥

ä½¿ç”¨`Statement`æˆ–`PreparedStatement`å¯¹è±¡æ‰§è¡Œ SQL è¯­å¥ã€‚

æ‰§è¡ŒæŸ¥è¯¢ï¼ˆSELECTï¼‰è¯­å¥æ—¶ï¼Œä½¿ç”¨`executeQuery()`æ–¹æ³•ï¼Œå®ƒè¿”å›`ResultSet`å¯¹è±¡ï¼›

æ‰§è¡Œæ›´æ–°ï¼ˆINSERTã€UPDATEã€DELETEï¼‰è¯­å¥æ—¶ï¼Œä½¿ç”¨`executeUpdate()`æ–¹æ³•ï¼Œå®ƒè¿”å›ä¸€ä¸ªæ•´æ•°è¡¨ç¤ºå—å½±å“çš„è¡Œæ•°ã€‚

    
    
    ResultSet rs = stmt.executeQuery("SELECT * FROM tableName");

æˆ–

    
    
    int affectedRows = stmt.executeUpdate("UPDATE tableName SET column = 'value' WHERE condition");

ç¬¬äº”æ­¥ï¼Œå¤„ç†ç»“æœé›†

å¦‚æœæ‰§è¡Œçš„æ˜¯æŸ¥è¯¢æ“ä½œï¼Œéœ€è¦å¤„ç†`ResultSet`å¯¹è±¡æ¥è·å–æ•°æ®ã€‚

    
    
    while (rs.next()) {
        String data = rs.getString("columnName");
        // å¤„ç†æ¯ä¸€è¡Œæ•°æ®
    }

ç¬¬å…­æ­¥ï¼Œå…³é—­èµ„æº

æœ€åï¼Œéœ€è¦ä¾æ¬¡å…³é—­`ResultSet`ã€`Statement`å’Œ`Connection`ç­‰èµ„æºï¼Œé‡Šæ”¾æ•°æ®åº“è¿æ¥ç­‰èµ„æºã€‚

    
    
    if (rs != null) rs.close();
    if (stmt != null) stmt.close();
    if (conn != null) conn.close();

åœ¨ Java å¼€å‘ä¸­ï¼Œé€šå¸¸ä¼šä½¿ç”¨ JDBC æ¨¡æ¿åº“ï¼ˆå¦‚ Spring çš„
JdbcTemplateï¼‰æˆ– ORM æ¡†æ¶ï¼ˆå¦‚ Hibernateã€MyBatisã€MyBatis-
Plusï¼‰æ¥ç®€åŒ–æ•°æ®åº“æ“ä½œå’Œèµ„æºç®¡ç†ã€‚

>   1. [Java
> é¢è¯•æŒ‡å—ï¼ˆä»˜è´¹ï¼‰](https://javabetter.cn/zhishixingqiu/mianshi.html)æ”¶å½•çš„äº¬ä¸œåŒå­¦
> 10 åç«¯å®ä¹ ä¸€é¢çš„åŸé¢˜ï¼šJDBC çš„æ‰§è¡Œæ­¥éª¤
>

### 22.åˆ›å»ºè¿æ¥æ‹¿åˆ°çš„æ˜¯ä»€ä¹ˆå¯¹è±¡ï¼Ÿ

åœ¨ JDBC
çš„æ‰§è¡Œæ­¥éª¤ä¸­ï¼Œåˆ›å»ºè¿æ¥åæ‹¿åˆ°çš„å¯¹è±¡æ˜¯`java.sql.Connection`å¯¹è±¡ã€‚è¿™ä¸ªå¯¹è±¡æ˜¯
JDBC API ä¸­ç”¨äºè¡¨ç¤ºæ•°æ®åº“è¿æ¥çš„æ¥å£ï¼Œå®ƒæä¾›äº†æ‰§è¡Œ SQL
è¯­å¥ã€ç®¡ç†äº‹åŠ¡ç­‰ä¸€ç³»åˆ—æ“ä½œçš„æ–¹æ³•ã€‚

`Connection`å¯¹è±¡ä»£è¡¨äº†åº”ç”¨ç¨‹åºå’Œæ•°æ®åº“çš„ä¸€ä¸ªè¿æ¥ä¼šè¯ã€‚

é€šè¿‡è°ƒç”¨`DriverManager.getConnection()`æ–¹æ³•å¹¶ä¼ å…¥æ•°æ®åº“çš„
URLã€ç”¨æˆ·åå’Œå¯†ç ç­‰ä¿¡æ¯æ¥è·å¾—è¿™ä¸ªå¯¹è±¡ã€‚

ä¸€æ—¦è·å¾—`Connection`å¯¹è±¡ï¼Œå°±å¯ä»¥ä½¿ç”¨å®ƒæ¥åˆ›å»ºæ‰§è¡Œ SQL
è¯­å¥çš„`Statement`ã€`PreparedStatement`å’Œ`CallableStatement`å¯¹è±¡ï¼Œä»¥åŠç®¡ç†äº‹åŠ¡ç­‰ã€‚

>   1. [Java
> é¢è¯•æŒ‡å—ï¼ˆä»˜è´¹ï¼‰](https://javabetter.cn/zhishixingqiu/mianshi.html)æ”¶å½•çš„äº¬ä¸œåŒå­¦
> 10 åç«¯å®ä¹ ä¸€é¢çš„åŸé¢˜ï¼šåˆ›å»ºè¿æ¥æ‹¿åˆ°çš„æ˜¯ä»€ä¹ˆå¯¹è±¡
>

### 23.Statement ä¸ PreparedStatement çš„åŒºåˆ«

> 2024 å¹´ 03 æœˆ 19 æ—¥å¢è¡¥

`Statement`å’Œ`PreparedStatement`éƒ½æ˜¯ç”¨äºæ‰§è¡Œ SQL
è¯­å¥çš„æ¥å£ï¼Œä½†å®ƒä»¬ä¹‹é—´å­˜åœ¨å‡ ä¸ªå…³é”®çš„åŒºåˆ«ï¼š

â‘
ã€æ¯æ¬¡æ‰§è¡Œ`Statement`å¯¹è±¡çš„`executeQuery`æˆ–`executeUpdate`æ–¹æ³•æ—¶ï¼ŒSQL
è¯­å¥åœ¨æ•°æ®åº“ç«¯éƒ½éœ€è¦é‡æ–°ç¼–è¯‘å’Œæ‰§è¡Œã€‚è¿™é€‚ç”¨äºä¸€æ¬¡æ€§æ‰§è¡Œçš„
SQL è¯­å¥ã€‚

**Statement** ä¸æ”¯æŒå‚æ•°åŒ–æŸ¥è¯¢ã€‚å¦‚æœéœ€è¦åœ¨ SQL
è¯­å¥ä¸­æ’å…¥å˜é‡ï¼Œé€šå¸¸éœ€è¦é€šè¿‡å­—ç¬¦ä¸²æ‹¼æ¥çš„æ–¹å¼æ¥å®ç°ï¼Œè¿™ä¼šå¢åŠ
SQL æ³¨å…¥æ”»å‡»çš„é£é™©ã€‚

â‘¡ã€**PreparedStatement** ä»£è¡¨é¢„ç¼–è¯‘çš„ SQL è¯­å¥çš„å¯¹è±¡ã€‚è¿™æ„å‘³ç€
SQL
è¯­å¥åœ¨`PreparedStatement`å¯¹è±¡åˆ›å»ºæ—¶å°±è¢«å‘é€åˆ°æ•°æ®åº“è¿›è¡Œé¢„ç¼–è¯‘ã€‚

ä¹‹åï¼Œå¯ä»¥é€šè¿‡è®¾ç½®å‚æ•°å€¼æ¥å¤šæ¬¡é«˜æ•ˆåœ°æ‰§è¡Œè¿™ä¸ª SQL
è¯­å¥ã€‚è¿™ä¸ä»…å‡å°‘äº†æ•°æ®åº“ç¼–è¯‘ SQL
è¯­å¥çš„å¼€é”€ï¼Œä¹Ÿæé«˜äº†æ€§èƒ½ï¼Œå°¤å…¶æ˜¯å¯¹äºé‡å¤æ‰§è¡Œçš„ SQL æ“ä½œã€‚

**PreparedStatement** æ”¯æŒå‚æ•°åŒ–æŸ¥è¯¢ï¼Œå³å¯ä»¥åœ¨ SQL
è¯­å¥ä¸­ä½¿ç”¨é—®å·ï¼ˆ`?`ï¼‰ä½œä¸ºå‚æ•°å
ä½ç¬¦ã€‚é€šè¿‡`setXxx`æ–¹æ³•ï¼ˆå¦‚`setString`ã€`setInt`ï¼‰è®¾ç½®å‚æ•°ï¼Œå¯ä»¥æœ‰æ•ˆé˜²æ­¢
SQL æ³¨å…¥ã€‚

æ€»çš„æ¥è¯´ï¼Œ`PreparedStatement`ç›¸æ¯”`Statement`æœ‰ç€æ›´å¥½çš„æ€§èƒ½å’Œæ›´é«˜çš„å®‰å…¨æ€§ï¼Œæ˜¯æ‰§è¡Œ
SQL
è¯­å¥çš„é¦–é€‰æ–¹å¼ï¼Œå°¤å…¶æ˜¯åœ¨å¤„ç†å«æœ‰ç”¨æˆ·è¾“å…¥çš„åŠ¨æ€æŸ¥è¯¢æ—¶ã€‚

>   1. [Java
> é¢è¯•æŒ‡å—ï¼ˆä»˜è´¹ï¼‰](https://javabetter.cn/zhishixingqiu/mianshi.html)æ”¶å½•çš„äº¬ä¸œåŒå­¦
> 10 åç«¯å®ä¹ ä¸€é¢çš„åŸé¢˜ï¼šstatement å’Œ preparedstatement çš„åŒºåˆ«
>

### 24\. ä»€ä¹ˆæ˜¯ SQL æ³¨å…¥ï¼Ÿå¦‚ä½•é˜²æ­¢ SQL æ³¨å…¥ï¼Ÿ

SQL æ³¨å…¥æ˜¯ä¸€ç§ä»£ç æ³¨å…¥æŠ€æœ¯ï¼Œé€šè¿‡åœ¨è¾“å…¥å­—æ®µä¸­æ’å…¥ä¸“ç”¨çš„
SQL è¯­å¥ï¼Œä»è€Œæ¬ºéª—æ•°æ®åº“æ‰§è¡Œæ¶æ„
SQLï¼Œä»¥è·å–æ•æ„Ÿæ•°æ®ã€ä¿®æ”¹æ•°æ®ï¼Œæˆ–è€…åˆ é™¤æ•°æ®ç­‰ã€‚

æ¯”å¦‚è¯´æœ‰è¿™æ ·ä¸€æ®µä»£ç ï¼š

    
    
    studentId = getRequestString("studentId");
    lookupStudent  = "SELECT * FROM students WHERE studentId = " + studentId

ç”¨æˆ·åœ¨è¾“å…¥æ¡†ä¸­è¾“å…¥ 117 è¿›è¡ŒæŸ¥è¯¢ï¼š

![cloudflareï¼šSQL
æŸ¥è¯¢](https://cdn.tobebetterjavaer.com/stutymore/mybatis-20240418100433.png)cloudflareï¼šSQL
æŸ¥è¯¢

å®é™…çš„ SQL è¯­å¥ç±»ä¼¼äºï¼š

    
    
    SELECT * FROM students WHERE studentId = 117

è¿™æ˜¯æˆ‘ä»¬æœŸæœ›ç”¨æˆ·è¾“å…¥çš„æ­£ç¡®æ–¹å¼ã€‚ä½†æ˜¯ï¼Œå¦‚æœç”¨æˆ·è¾“å…¥äº†`117
OR 1=1`ï¼Œé‚£ä¹ˆ SQL è¯­å¥å°±å˜æˆäº†ï¼š

    
    
    SELECT * FROM students WHERE studentId = 117 OR 1=1

ç”±äº`1=1`ä¸ºçœŸï¼Œæ‰€ä»¥è¿™ä¸ªæŸ¥è¯¢å°†è¿”å›æ‰€æœ‰å­¦ç”Ÿçš„ä¿¡æ¯ï¼Œè€Œä¸ä»…ä»…æ˜¯
ID ä¸º 117 çš„å­¦ç”Ÿã€‚

![cloudflareï¼šSQL
æ³¨å…¥](https://cdn.tobebetterjavaer.com/stutymore/mybatis-20240418100940.png)cloudflareï¼šSQL
æ³¨å…¥

ä¸ºäº†é˜²æ­¢ SQL æ³¨å…¥ï¼Œå¯ä»¥é‡‡å–ä»¥ä¸‹æªæ–½ï¼š

â‘ ã€ä½¿ç”¨å‚æ•°åŒ–æŸ¥è¯¢

ä½¿ç”¨å‚æ•°åŒ–æŸ¥è¯¢ï¼Œå³ä½¿ç”¨`PreparedStatement`å¯¹è±¡ï¼Œé€šè¿‡`setXxx`æ–¹æ³•è®¾ç½®å‚æ•°å€¼ï¼Œè€Œä¸æ˜¯é€šè¿‡å­—ç¬¦ä¸²æ‹¼æ¥
SQL è¯­å¥ã€‚è¿™æ ·å¯ä»¥æœ‰æ•ˆé˜²æ­¢ SQL æ³¨å…¥ã€‚

    
    
    String query = "SELECT * FROM users WHERE username = ?";
    PreparedStatement pstmt = connection.prepareStatement(query);
    pstmt.setString(1, userName);  // userName æ˜¯ç”¨æˆ·è¾“å…¥
    ResultSet rs = pstmt.executeQuery();

`?` æ˜¯ä¸€ä¸ªå‚æ•°å ä½ç¬¦ï¼ŒuserName æ˜¯å¤–éƒ¨è¾“å…¥ã€‚è¿™æ
·å³ä¾¿ç”¨æˆ·è¾“å…¥äº†æ¶æ„çš„ SQL
è¯­å¥ï¼Œä¹Ÿåªä¼šè¢«è§†ä¸ºå‚æ•°çš„ä¸€éƒ¨åˆ†ï¼Œä¸ä¼šæ”¹å˜æŸ¥è¯¢çš„ç»“æ„ã€‚

â‘¡ã€é™åˆ¶ç”¨æˆ·è¾“å…¥

å¯¹ç”¨æˆ·è¾“å…¥è¿›è¡ŒéªŒè¯å’Œè¿‡æ»¤ï¼Œåªå…è®¸è¾“å…¥é¢„æœŸçš„æ•°æ®ï¼Œä¸å…è®¸è¾“å…¥ç‰¹æ®Šå­—ç¬¦æˆ–
SQL å…³é”®å­—ã€‚

â‘¢ã€ä½¿ç”¨ ORM æ¡†æ¶

æ¯”å¦‚ï¼Œåœ¨ MyBatis ä¸­ï¼Œä½¿ç”¨`#{}`å ä½ç¬¦æ¥ä»£æ›¿ç›´æ¥æ‹¼æ¥ SQL
è¯­å¥ï¼ŒMyBatis ä¼šè‡ªåŠ¨è¿›è¡Œå‚æ•°åŒ–å¤„ç†ã€‚

    
    
    <select id="selectUser" resultType="User">
      SELECT * FROM users WHERE username = #{userName}
    </select>

å‡å¦‚ userName ä¼ å…¥çš„å€¼æ˜¯ `9;DROP TABLE SYS_USER;`ï¼Œä¼ å…¥çš„åˆ é™¤è¡¨
SQL ä¹Ÿä¸ä¼šæ‰§è¡Œï¼Œå› ä¸ºå®ƒä¼šè¢«å½“ä½œå‚æ•°å€¼ã€‚

    
    
    SELECT * FROM users WHERE username = '9;DROP TABLE SYS_USER;'

>   1. [Java
> é¢è¯•æŒ‡å—ï¼ˆä»˜è´¹ï¼‰](https://javabetter.cn/zhishixingqiu/mianshi.html)æ”¶å½•çš„å­—èŠ‚è·³åŠ¨é¢ç»åŒå­¦
> 13 Java åç«¯äºŒé¢é¢è¯•åŸé¢˜ï¼šä»€ä¹ˆæ˜¯ SQL
> æ³¨å…¥ï¼Œæ€ä¹ˆé¿å…ï¼Œä»€ä¹ˆæ˜¯å‚æ•°åŒ–
>   2. [Java
> é¢è¯•æŒ‡å—ï¼ˆä»˜è´¹ï¼‰](https://javabetter.cn/zhishixingqiu/mianshi.html)æ”¶å½•çš„åŒå­¦
> 30 è…¾è®¯éŸ³ä¹é¢è¯•åŸé¢˜ï¼šå¦‚ä½•é˜²èŒƒsqlçš„æ³¨å…¥æ”»å‡»å‘¢ï¼Ÿ
>

* * *

å›¾æ–‡è¯¦è§£ 23 é“ MyBatis
é¢è¯•é«˜é¢‘é¢˜ï¼Œè¿™æ¬¡åŠæ‰“é¢è¯•å®˜ï¼Œæˆ‘è§‰å¾—ç¨³äº†ï¼ˆæ‰‹åŠ¨
dogï¼‰ã€‚æ•´ç†ï¼šæ²‰é»˜ç‹äºŒï¼Œæˆ³[è½¬è½½é“¾æ¥](https://mp.weixin.qq.com/s/en2RgcVx52Ql3tYGLfv3Kw)ï¼Œä½œè€…ï¼šä¸‰åˆ†æ¶ï¼Œæˆ³[åŸæ–‡é“¾æ¥](https://mp.weixin.qq.com/s/O_5Id2o9IP4loPazJuiHng)ã€‚

_æ²¡æœ‰ä»€ä¹ˆä½¿æˆ‘åœç•™â€”â€”é™¤äº†ç›®çš„ï¼Œçºµç„¶å²¸æ—æœ‰ç«ç‘°ã€æœ‰ç»¿è«ã€æœ‰å®é™çš„æ¸¯æ¹¾ï¼Œæˆ‘æ˜¯ä¸ç³»ä¹‹èˆŸ_
ã€‚

**ç³»åˆ—å†…å®¹** ï¼š

  * [é¢æ¸£é€†è¢­ Java SE ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/javase.html)
  * [é¢æ¸£é€†è¢­ Java é›†åˆæ¡†æ¶ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/javathread.html)
  * [é¢æ¸£é€†è¢­ Java å¹¶å‘ç¼–ç¨‹ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/collection.html)
  * [é¢æ¸£é€†è¢­ JVM ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/jvm.html)
  * [é¢æ¸£é€†è¢­ Spring ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/spring.html)
  * [é¢æ¸£é€†è¢­ Redis ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/redis.html)
  * [é¢æ¸£é€†è¢­ MyBatis ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/mybatis.html)
  * [é¢æ¸£é€†è¢­ MySQL ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/mysql.html)
  * [é¢æ¸£é€†è¢­æ“ä½œç³»ç»Ÿç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/os.html)
  * [é¢æ¸£é€†è¢­è®¡ç®—æœºç½‘ç»œç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/network.html)
  * [é¢æ¸£é€†è¢­ RocketMQ ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/rocketmq.html)
  * [é¢æ¸£é€†è¢­åˆ†å¸ƒå¼ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/fenbushi.html)
  * [é¢æ¸£é€†è¢­å¾®æœåŠ¡ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/weifuwu.html)
  * [é¢æ¸£é€†è¢­è®¾è®¡æ¨¡å¼ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/shejimoshi.html)
  * [é¢æ¸£é€†è¢­ Linux ç¯‡ ğŸ‘](https://javabetter.cn/sidebar/sanfene/linux.html)

* * *

GitHub ä¸Šæ ‡æ˜Ÿ 10000+ çš„å¼€æºçŸ¥è¯†åº“ã€Š[äºŒå“¥çš„ Java
è¿›é˜¶ä¹‹è·¯](https://github.com/itwanger/toBeBetterJavaer)ã€‹ç¬¬ä¸€ç‰ˆ PDF
ç»ˆäºæ¥äº†ï¼åŒ…æ‹¬ Java åŸºç¡€è¯­æ³•ã€æ•°ç»„&å­—ç¬¦ä¸²ã€OOPã€é›†åˆæ¡†æ¶ã€Java
IOã€å¼‚å¸¸å¤„ç†ã€Java æ–°ç‰¹æ€§ã€ç½‘ç»œç¼–ç¨‹ã€NIOã€å¹¶å‘ç¼–ç¨‹ã€JVM
ç­‰ç­‰ï¼Œå…±è®¡ 32 ä¸‡ä½™å­—ï¼Œ500+å¼
æ‰‹ç»˜å›¾ï¼Œå¯ä»¥è¯´æ˜¯é€šä¿—æ˜“æ‡‚ã€é£è¶£å¹½é»˜â€¦â€¦è¯¦æƒ…æˆ³ï¼š[å¤ªèµäº†ï¼ŒGitHub
ä¸Šæ ‡æ˜Ÿ 10000+ çš„ Java æ•™ç¨‹](https://javabetter.cn/overview/)

å¾®ä¿¡æœ **æ²‰é»˜ç‹äºŒ** æˆ–æ‰«æä¸‹æ–¹äºŒç»´ç
å…³æ³¨äºŒå“¥çš„åŸåˆ›å…¬ä¼—å·æ²‰é»˜ç‹äºŒï¼Œå›å¤ **222** å³å¯å…è´¹é¢†å–ã€‚

![](https://cdn.tobebetterjavaer.com/tobebetterjavaer/images/gongzhonghao.png)

[åœ¨ GitHub
ä¸Šç¼–è¾‘æ­¤é¡µ](https://github.com/itwanger/toBeBetterJavaer/edit/master/docs/src/sidebar/sanfene/mybatis.md)

ä¸Šæ¬¡ç¼–è¾‘äº:

è´¡çŒ®è€…: æ²‰é»˜ç‹äºŒ

[ä¸Šä¸€é¡µé¢æ¸£é€†è¢­-Redis](/sidebar/sanfene/redis.html)[ä¸‹ä¸€é¡µé¢æ¸£é€†è¢­-MySQL](/sidebar/sanfene/mysql.html)

