import java.util.HashMap;
import java.util.LinkedHashMap;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int photoLen = photo.length;
        int nameLen = name.length;
        int[] answer = new int[photoLen];
        
        HashMap<String,Integer> map = new LinkedHashMap<>();
        for (int i = 0; i < nameLen; i++) {
            map.put(name[i], yearning[i]);
        }
        
        for (int i = 0; i < photoLen; i++) {
            String[] persons = photo[i];
            int score = 0;
            
            for (int j = 0; j < persons.length; j++) {
                String person = persons[j];
                if (map.containsKey(person)) {
                    score += map.get(person);
                }
            }
            
            answer[i] = score;
        }
        
        return answer;
    }
}