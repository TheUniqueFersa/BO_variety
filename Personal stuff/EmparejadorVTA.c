#include <stdio.h>

int main(void) {
  float dinero=0, seycel = 0, otro=0, resta=0, original_resta=0, resta_orig_dinero=0, dinero_igual_para_ambas=0;
  float total_seycel=0, total_otro=0;
  printf("Que hongo pinxe Ferson, caele con las cantidades en corto: \n");
  printf("Cuanto baro tienes pa? ");
  scanf("%f", &dinero);
  printf("SEYCEL: ");
  scanf("%f", &seycel);
  printf("\nEl otro XD: ");
  scanf("%f", &otro);
  resta = seycel - otro;
  if(resta != 0){
    if(resta<0)
      resta*=-1;
    original_resta=resta/1.0625;
    resta_orig_dinero=dinero-original_resta;
    dinero_igual_para_ambas=resta_orig_dinero/2;
    total_seycel=dinero_igual_para_ambas+original_resta;
    total_otro=dinero_igual_para_ambas;
    //pendiente dar el nombre correcto en las cantidades    
  }
  else{
    total_seycel=dinero/2;
    total_otro=dinero/2;
  }  
  printf("Perverso, las cantidades son:\n1: %.2f\n2: %.2f", total_seycel, total_otro);
  return 0;
}