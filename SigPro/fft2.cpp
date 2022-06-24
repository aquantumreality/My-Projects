#define PI 3.14159


struct sp_cmplx{
    float r = 0.0, c = 0.0;
};

void twoPtDFT(sp_cmplx *x, sp_cmplx *X, int sample_size){
    // X[0] = x[0] + x[1]
    // X[1] = x[0] - x[1]
    int id = blockIdx.x*blockDim.x + threadIdx.x;

    X[2*id].r = x[2*id].r + x[2*id + sample_size/2].r;
    X[2*id].c = x[2*id].c + x[2*id + sample_size/2].c;

    X[2*id + 1].r = x[2*id].r - x[2*id + sample_size/2].r;
    X[2*id + 1].c = x[2*id].c - x[2*id + sample_size/2].c;
}

void combine(sp_cmplx *X, int ptBy4, int sample_size){
    int id = blockIdx.x*blockDim.x + threadIdx.x;
    int sample_index = (id/(ptBy4))*ptBy4 + (id%ptBy4);

    sp_cmplx in1 = X[sample_index];
    sp_cmplx in2 = X[sample_index + int(log2(ptBy4)) + 1];

    X[sample_index].r = in1.r + cos(8*PI*((float)id)/ptBy4)in2.r - sin(8*PI((float)id)/ptBy4)*in2.c;
    X[sample_index].c = in1.c + cos(8*PI*((float)id)/ptBy4)in2.c + sin(8*PI((float)id)/ptBy4)*in2.r;

    X[sample_index + int(log2(ptBy4)) + 1].r = in1.r + cos(8*PI*((float)id)/ptBy4)in2.r - sin(8*PI((float)id)/ptBy4)*in2.c;
    X[sample_index + int(log2(ptBy4)) + 1].c = in1.c + cos(8*PI*((float)id)/ptBy4)in2.c + sin(8*PI((float)id)/ptBy4)*in2.r;
}