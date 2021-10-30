public class MyTest {
    public void show(String name){
        Jsoup.parse(File in, String charsetName);
        Jsoup.parse(File in, String charsetName, String baseUri);
        
        File input = new File("../tmp/input.html");
        Document doc = Jsoup.parse(input, "UTF-8", "http://adamsun.com/");
    }
}
