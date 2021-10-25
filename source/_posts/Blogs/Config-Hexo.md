---
date: 2021-04-7 00:40:12
title: "Config-Hexo"
mathjax: false
toc: true
categories: [Blogs]
---
***

## Summary

<!-- more -->

### 修改Recent_Post 的数量
```javascript node_modules/hexo-component-inferno/lib/view/widget/recent_posts.js
var site = props.site,
      helper = props.helper,
      _props$limit = props.limit,
-     limit = _props$limit === void 0 ? 5 : _props$limit;
+     limit = _props$limit === void 0 ? 4 : _props$limit;
  var url_for = helper.url_for,
      __ = helper.__,
      date_xml = helper.date_xml,
      date = helper.date;

  if (!site.posts.length) {
    return null;
  }
```