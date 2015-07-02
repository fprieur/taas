casper.test.begin('click tests', 1, function(test) {
    
    casper.start("https://example.com", function() {
        this.click("h1"); 
    });
    
    casper.then(function() {
        test.assertEquals(this.getCurrentUrl(), "https://www.google.com/doodles", "expected url is correct");
    });

    casper.run(function() {
        test.done()
    });
});
