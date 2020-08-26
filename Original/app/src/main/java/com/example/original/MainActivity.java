package com.example.original;

import android.os.Bundle;


import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONArray;


public class MainActivity extends AppCompatActivity {
    public JSONArray attempts = new JSONArray();

    public String filename = "";
    public int session = 0;
    public int attempt = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
