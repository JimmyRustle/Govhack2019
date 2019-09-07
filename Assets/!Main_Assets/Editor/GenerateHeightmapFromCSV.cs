using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using UnityEngine.Windows;
using System.IO;

public static class MenuFunctions
{
    public static ushort texSize = 2048;
    public static ushort[] dummyData = LoadData();
    
    public static ushort[] GenerateDummyData(ushort size = 512)
    {
        ushort[] returnVal = new ushort[size*size];

        for (ushort i = 0; i < size * size; i++)
        {
           returnVal[i] = (ushort)Random.Range(0, 5048);
        }

        return returnVal;
    }

    public static ushort[] LoadData()
    {
        ushort[] returnVal = new ushort[texSize * texSize];
        string path = Application.dataPath + "/!Main_Assets/TestHeightmaps/gbr30_water_2048x2048.txt";
        using (var reader = new StreamReader(path))
        {
            int linesRead = 0;
            float min = float.MaxValue;
            float max = 0;
            while (!reader.EndOfStream)
            {
                var line = reader.ReadLine();
                var values = line.Split(',');
                for (int i = 0; i < values.Length-1; i++)
                {
                    float height = float.Parse(values[i]);
                    min = Mathf.Min(min, height);
                    max = Mathf.Max(max, height);
                    returnVal[linesRead++] = (ushort)(float.Parse(values[i]) * 100);
                }
            }
            Debug.Log("Min: " + min + ", Max: " + max);
        }
        return returnVal;
    }

    public static float Scale01(float value, float min, float max)
    {
        float returnVal = value;
        returnVal = Mathf.Clamp01( (value - min) / (max - min));
        return returnVal;
    }


    [MenuItem("Window/CreateHeightmap")]
    public static void CreateHeightmapFromCSV()
    {
        //dummyData = GenerateDummyData(texSize);
        //Texture2D newTex = new Texture2D(texSize, texSize, TextureFormat.R16, false);
        ushort[] singleArray = LoadData();
        //Unity.Collections.NativeArray<ushort> array = new Unity.Collections.NativeArray<ushort>(singleArray, Unity.Collections.Allocator.Temp);

        byte[] result = new byte[singleArray.Length * sizeof(ushort)];
        System.Buffer.BlockCopy(singleArray, 0, result, 0, result.Length);

        //newTex.LoadRawTextureData(array);

        string path = Application.dataPath + "/!Main_Assets/TestHeightmaps/heightmap.raw";
        UnityEngine.Windows.File.WriteAllBytes(path, result);
        //File.WriteAllBytes(path, newTex.GetRawTextureData());
        AssetDatabase.ImportAsset("assets/!Main_Assets/TestHeightmaps/heightmap.raw", ImportAssetOptions.ForceUpdate);
    }
    static ushort[] MultiToSingle(ushort[,] array)
    {
        ushort index = 0;
        ushort width = (ushort)array.GetLength(0);
        ushort height = (ushort)array.GetLength(1);
        ushort[] single = new ushort[width * height];
        for (ushort y = 0; y < height; y++)
        {
            for (ushort x = 0; x < width; x++)
            {
                single[index] = array[x, y];
                index++;
            }
        }
        return single;
    }

    [ContextMenu("Generate Heightmap", true)]
    public static bool CreateHeightmapValidation()
    {
        return false;
    }
}
